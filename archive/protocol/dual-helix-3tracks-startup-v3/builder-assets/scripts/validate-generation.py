#!/usr/bin/env python3
"""
Generation Validator
Checks for common template failures and generation issues.

This validator catches:
1. Unreplaced placeholders like [Project Name], {domain-role-id}
2. Encoding issues (corrupted emojis, weird characters)
3. Structural problems (missing required sections)
"""

import os
import sys
import re
import json
from pathlib import Path

# Common placeholder patterns that should NEVER appear in final output
PLACEHOLDER_PATTERNS = [
    r'\[Project Name\]',
    r'\[Domain Role Name\]',
    r'\[Domain Role\]',
    r'\[domain-role-id\]',
    r'\[domain-id\]',
    r'\[domain\]',
    r'\[Agent Name\]',
    r'\[Date\]',
    r'\[TOPIC\]',
    r'\[SKILL_NAME\]',
    r'\[BEHAVIOR_NAME\]',
    r'\[behavior-id\]',
    r'\[Behavior Name\]',
    r'\[category\]',
    r'\[skill-id\]',
    r'\[Skill Name\]',
    r'\{DOMAIN_ROLE_ID\}',  # Template variable syntax
    r'\{PROJECT_NAME\}',
    r'\{DOMAIN_ID\}',
    r'\[protocol-path\]',
    r'\[project name from Phase 1\]',
    r'\[from Phase \d+\]',
]

# Encoding issues - corrupted characters
ENCODING_ISSUES = [
    r'ðŸ',  # Corrupted emoji prefix
    r'â',   # Corrupted special char
    r'Ã',   # UTF-8 mojibake
    r'Â',   # UTF-8 mojibake
    r'\\x[0-9a-fA-F]{2}',  # Hex escapes
]

# Required content patterns for specific file types
REQUIRED_PATTERNS = {
    'visualization.html': [
        r'vis-network',  # Must use vis-network library
        r'loadGraph',    # Must have graph loading function
        r'master-graph\.json',  # Must reference master graph
    ],
    'master-graph.json': [
        r'"graphType":\s*"master"',
        r'"graphs"',
        r'"roles"',
    ],
    '*-knowledge-graph.json': [
        r'"graphType":\s*"knowledge"',
        r'"nodes"',
        r'"type":\s*"root"',
    ],
    '*-skills-graph.json': [
        r'"graphType":\s*"skills"',
        r'"skills"|"nodes"',
        r'"type":\s*"root"',
    ],
    '*-behaviors-graph.json': [
        r'"graphType":\s*"behaviors"',
        r'"behaviors"|"nodes"',
        r'"type":\s*"root"',
    ],
}

class ValidationResult:
    def __init__(self, filename):
        self.filename = filename
        self.errors = []
        self.warnings = []
        
    def add_error(self, msg):
        self.errors.append(msg)
        
    def add_warning(self, msg):
        self.warnings.append(msg)
        
    def is_valid(self):
        return len(self.errors) == 0
        
    def __str__(self):
        lines = [f"\n{'='*60}", f"File: {self.filename}"]
        if self.errors:
            lines.append(f"  ❌ ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"     • {e}")
        if self.warnings:
            lines.append(f"  ⚠️  WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"     • {w}")
        if not self.errors and not self.warnings:
            lines.append("  ✅ Valid")
        return '\n'.join(lines)


def check_placeholders(content, result):
    """Check for unreplaced placeholder text"""
    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            result.add_error(f"Unreplaced placeholder: {matches[0]}")


def check_encoding(content, result):
    """Check for encoding corruption"""
    for pattern in ENCODING_ISSUES:
        matches = re.findall(pattern, content)
        if matches:
            # Show context around the issue
            for match in matches[:3]:  # Limit to first 3
                idx = content.find(match)
                context = content[max(0, idx-20):idx+30]
                result.add_error(f"Encoding issue near: ...{context}...")


def check_json_validity(content, result):
    """Check if JSON is valid"""
    try:
        data = json.loads(content)
        return data
    except json.JSONDecodeError as e:
        result.add_error(f"Invalid JSON: {e}")
        return None


def check_graph_structure(data, result):
    """Check Knowledge Graph structural requirements"""
    if not data:
        return
    
    # Master graphs have 'graphs' instead of 'nodes'
    if data.get('graphType') == 'master':
        if not data.get('graphs'):
            result.add_warning("Master graph missing 'graphs' array")
        if not data.get('roles'):
            result.add_warning("Master graph missing 'roles' array")
        return
        
    # Find nodes array (could be nodes, skills, or behaviors)
    nodes = data.get('nodes') or data.get('skills') or data.get('behaviors') or []
    
    if not nodes:
        result.add_warning("No nodes found in graph")
        return
        
    # Check for root node
    root_nodes = [n for n in nodes if n.get('type') == 'root']
    if len(root_nodes) == 0:
        result.add_error("No root node found (type: 'root')")
    elif len(root_nodes) > 1:
        result.add_warning(f"Multiple root nodes found: {[n.get('id') for n in root_nodes]}")
        
    # Check parent links
    all_ids = {n.get('id') for n in nodes}
    for node in nodes:
        node_id = node.get('id', 'unknown')
        node_type = node.get('type', '')
        
        if node_type != 'root' and 'parent' not in node:
            result.add_error(f"Node '{node_id}' missing parent field (V2 requirement)")
            
        parent = node.get('parent')
        if parent and parent not in all_ids:
            result.add_error(f"Node '{node_id}' has invalid parent: '{parent}'")


def check_required_patterns(content, filename, result):
    """Check file-type-specific required content"""
    for pattern_key, patterns in REQUIRED_PATTERNS.items():
        # Check if this file matches the pattern key
        if pattern_key.startswith('*'):
            suffix = pattern_key[1:]
            if not filename.endswith(suffix):
                continue
        elif filename != pattern_key:
            continue
            
        # Check each required pattern
        for pattern in patterns:
            if not re.search(pattern, content):
                result.add_warning(f"Missing expected pattern: {pattern}")


def validate_file(filepath):
    """Validate a single file"""
    result = ValidationResult(filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result.add_error(f"Could not read file: {e}")
        return result
        
    filename = os.path.basename(filepath)
    
    # Check for placeholders
    check_placeholders(content, result)
    
    # Check for encoding issues
    check_encoding(content, result)
    
    # File-type specific checks
    if filepath.endswith('.json'):
        data = check_json_validity(content, result)
        if data and 'graphType' in data:
            check_graph_structure(data, result)
    
    # Check required patterns
    check_required_patterns(content, filename, result)
    
    return result


def validate_directory(dirpath, extensions=None):
    """Validate all files in a directory"""
    if extensions is None:
        extensions = ['.json', '.html', '.md']
        
    results = []
    path = Path(dirpath)
    
    for ext in extensions:
        for filepath in path.rglob(f'*{ext}'):
            # Skip templates and specifications (they contain placeholder examples)
            if '.template' in str(filepath):
                continue
            if '.spec.md' in str(filepath):
                continue
            if '/specs/' in str(filepath):
                continue
            results.append(validate_file(str(filepath)))
            
    return results


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python validate_generation.py <file_or_directory>")
        print("\nValidates generated files for common issues:")
        print("  - Unreplaced placeholders")
        print("  - Encoding corruption")
        print("  - JSON structure (for KG files)")
        print("  - Required content patterns")
        sys.exit(1)
        
    target = sys.argv[1]
    
    if os.path.isfile(target):
        results = [validate_file(target)]
    elif os.path.isdir(target):
        results = validate_directory(target)
    else:
        print(f"Error: {target} not found")
        sys.exit(1)
        
    # Print results
    print("\n" + "="*60)
    print("GENERATION VALIDATION REPORT")
    print("="*60)
    
    errors = 0
    warnings = 0
    
    for result in results:
        print(result)
        errors += len(result.errors)
        warnings += len(result.warnings)
        
    print("\n" + "="*60)
    print(f"SUMMARY: {len(results)} files checked")
    print(f"  Errors: {errors}")
    print(f"  Warnings: {warnings}")
    
    if errors > 0:
        print("\n❌ VALIDATION FAILED - Fix errors before proceeding")
        sys.exit(1)
    elif warnings > 0:
        print("\n⚠️  Validation passed with warnings")
        sys.exit(0)
    else:
        print("\n✅ All files valid!")
        sys.exit(0)


if __name__ == '__main__':
    main()