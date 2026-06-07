#!/usr/bin/env python3
"""
Validate Document Chunking Compliance

Validates that AI-consumed documents follow chunking best practices:
- File size: 250-500 lines (1.5k-3k tokens)
- One concept per file
- Concept/execution separation
- Cross-linking instead of duplication

Usage:
    python validate_chunking.py <path>
    python validate_chunking.py <path> --recursive
    python validate_chunking.py <path> --output report.json
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Configuration
IDEAL_MIN_LINES = 250
IDEAL_MAX_LINES = 350
ACCEPTABLE_MAX_LINES = 500
OVERSIZED_THRESHOLD = 501

# Document type patterns
AI_CONSUMED_PATHS = [
    "docs/",
    "agents/skills/",
    ".cursor/behaviors/",
]

HUMAN_CONSUMED_PATTERNS = [
    "USER_MANUAL",
    "README",
    "_DESIGN_SUMMARY",
    "WALKTHROUGH",
]

AI_CONSUMED_TYPES = ["skill", "behavior", "knowledge"]


def count_lines(file_path: str) -> int:
    """Count non-empty lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Count non-empty lines
            return sum(1 for line in lines if line.strip())
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return 0


def estimate_tokens(line_count: int) -> int:
    """Estimate token count from line count (rough: ~5 tokens per line)."""
    return line_count * 5


def parse_frontmatter(file_path: str) -> Dict:
    """Parse YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for frontmatter
        if not content.startswith('---'):
            return {}
        
        # Extract frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}
        
        frontmatter_text = parts[1].strip()
        
        # Simple YAML parsing (key: value)
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle lists
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip().strip('"\'') for v in value[1:-1].split(',')]
                else:
                    value = value.strip('"\'')
                
                frontmatter[key] = value
        
        return frontmatter
    except Exception as e:
        print(f"Error parsing frontmatter in {file_path}: {e}", file=sys.stderr)
        return {}


def find_markdown_links(file_path: str) -> List[str]:
    """Find all markdown links in file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find markdown links: [text](url)
        pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        matches = re.findall(pattern, content)
        
        # Return URLs
        return [url for _, url in matches]
    except Exception as e:
        print(f"Error finding links in {file_path}: {e}", file=sys.stderr)
        return []


def classify_document(file_path: str) -> str:
    """Classify document as ai-consumed, human-consumed, or unknown."""
    file_name = os.path.basename(file_path)
    
    # Check human-consumed patterns
    for pattern in HUMAN_CONSUMED_PATTERNS:
        if pattern in file_name:
            return "human-consumed"
    
    # Check AI-consumed paths
    for path_prefix in AI_CONSUMED_PATHS:
        if path_prefix in file_path.replace('\\', '/'):
            return "ai-consumed"
    
    # Check frontmatter
    frontmatter = parse_frontmatter(file_path)
    if frontmatter.get("type") in AI_CONSUMED_TYPES:
        return "ai-consumed"
    
    return "unknown"


def validate_file_size(line_count: int) -> Tuple[str, Optional[Dict]]:
    """Validate file size against chunking rules."""
    if line_count > OVERSIZED_THRESHOLD:
        return "error", {
            "rule": "file-size",
            "severity": "error",
            "message": f"File exceeds {ACCEPTABLE_MAX_LINES}-line recommendation ({line_count} lines)",
            "recommendation": "Split into smaller files (250-500 lines each)"
        }
    elif line_count > IDEAL_MAX_LINES:
        return "warning", {
            "rule": "file-size",
            "severity": "warning",
            "message": f"File is acceptable but larger than ideal ({line_count} lines)",
            "recommendation": "Consider splitting if adding more content"
        }
    elif line_count < IDEAL_MIN_LINES:
        return "info", {
            "rule": "file-size",
            "severity": "info",
            "message": f"File is smaller than ideal range ({line_count} lines)",
            "recommendation": "This is fine for simple concepts"
        }
    else:
        return "ok", None


def validate_concept_boundary(file_path: str) -> Tuple[str, Optional[Dict]]:
    """Validate that file has single concept."""
    frontmatter = parse_frontmatter(file_path)
    
    if "category" in frontmatter:
        category = frontmatter["category"]
        if isinstance(category, list) and len(category) > 1:
            return "warning", {
                "rule": "concept-boundary",
                "severity": "warning",
                "message": f"File has multiple categories: {', '.join(category)}",
                "recommendation": "Consider splitting into separate files per category"
            }
    
    return "ok", None


def validate_cross_linking(file_path: str, line_count: int) -> Tuple[str, Optional[Dict]]:
    """Validate cross-linking for large files."""
    if line_count < 400:
        return "ok", None
    
    links = find_markdown_links(file_path)
    
    # Filter for relative links (internal cross-links)
    internal_links = [link for link in links if not link.startswith(('http://', 'https://', '#'))]
    
    if len(internal_links) == 0:
        return "warning", {
            "rule": "cross-linking",
            "severity": "warning",
            "message": "Large file with no cross-links to related files",
            "recommendation": "Consider if content should be split and cross-linked"
        }
    
    return "ok", None


def validate_file(file_path: str) -> Dict:
    """Validate a single file against chunking rules."""
    # Classify document type
    doc_type = classify_document(file_path)
    
    if doc_type == "human-consumed":
        return {
            "file": file_path,
            "documentType": doc_type,
            "status": "skipped",
            "reason": "Human-consumed document (chunking rules don't apply)"
        }
    
    # Count lines
    line_count = count_lines(file_path)
    token_estimate = estimate_tokens(line_count)
    
    # Run validation rules
    issues = []
    
    # Rule 1: File size
    status, issue = validate_file_size(line_count)
    if issue:
        issues.append(issue)
    
    # Rule 2: Concept boundary
    status, issue = validate_concept_boundary(file_path)
    if issue:
        issues.append(issue)
    
    # Rule 3: Cross-linking
    status, issue = validate_cross_linking(file_path, line_count)
    if issue:
        issues.append(issue)
    
    # Determine overall status
    if any(i["severity"] == "error" for i in issues):
        overall_status = "oversized"
    elif any(i["severity"] == "warning" for i in issues):
        overall_status = "acceptable"
    else:
        overall_status = "compliant"
    
    return {
        "file": file_path,
        "documentType": doc_type,
        "lines": line_count,
        "tokens": token_estimate,
        "status": overall_status,
        "issues": issues
    }


def validate_folder(folder_path: str, recursive: bool = False) -> Dict:
    """Validate all markdown files in a folder."""
    results = []
    
    # Find all .md files
    if recursive:
        md_files = list(Path(folder_path).rglob("*.md"))
    else:
        md_files = list(Path(folder_path).glob("*.md"))
    
    # Validate each file
    for md_file in md_files:
        result = validate_file(str(md_file))
        results.append(result)
    
    # Generate summary
    total_files = len(results)
    ai_consumed = sum(1 for r in results if r["documentType"] == "ai-consumed")
    human_consumed = sum(1 for r in results if r["documentType"] == "human-consumed")
    
    compliant = sum(1 for r in results if r.get("status") == "compliant")
    acceptable = sum(1 for r in results if r.get("status") == "acceptable")
    oversized = sum(1 for r in results if r.get("status") == "oversized")
    skipped = sum(1 for r in results if r.get("status") == "skipped")
    
    oversized_files = [
        {
            "file": r["file"],
            "lines": r["lines"],
            "recommendation": r["issues"][0]["recommendation"] if r.get("issues") else None
        }
        for r in results if r.get("status") == "oversized"
    ]
    
    return {
        "folder": folder_path,
        "totalFiles": total_files,
        "aiConsumedFiles": ai_consumed,
        "humanConsumedFiles": human_consumed,
        "summary": {
            "compliant": compliant,
            "acceptable": acceptable,
            "oversized": oversized,
            "skipped": skipped
        },
        "oversizedFiles": oversized_files,
        "details": results
    }


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate document chunking compliance"
    )
    parser.add_argument(
        "path",
        help="File or folder path to validate"
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Recursively validate all subfolders"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output JSON file path (default: stdout)"
    )
    
    args = parser.parse_args()
    
    # Check if path exists
    if not os.path.exists(args.path):
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        sys.exit(1)
    
    # Validate
    if os.path.isfile(args.path):
        result = validate_file(args.path)
    else:
        result = validate_folder(args.path, recursive=args.recursive)
    
    # Output
    json_output = json.dumps(result, indent=2)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(json_output)
        print(f"Results written to: {args.output}")
    else:
        print(json_output)
    
    # Exit code based on status
    if isinstance(result, dict):
        if result.get("status") == "oversized":
            sys.exit(1)
        elif result.get("summary", {}).get("oversized", 0) > 0:
            sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
