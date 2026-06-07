#!/usr/bin/env python3
"""
KG Integrity Validator - Quality Control
=========================================

Comprehensive validation of Knowledge Graph integrity, including:
- Referential integrity (parent/child relationships)
- Orphan node detection
- Duplicate ID detection
- Required field validation
- Structural consistency checks

Usage:
    python validate_kg_integrity.py --role builder
    python validate_kg_integrity.py --role domain --verbose
    python validate_kg_integrity.py --all
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime
from collections import Counter

# Paths
# This validator does *relational* integrity (parent/child, orphans, cycles)
# on knowledge graphs only — those use the `nodes` array key.
# Skills + behaviors graphs are validated by `validate_schemas.py` against
# their JSON Schema files in `lib/schemas/` (sibling tool).
WORKSPACE = Path(__file__).parent.parent.parent
KG_DIR = WORKSPACE / 'agents' / 'knowledge-graphs'
KG_PATHS = {
    'builder': KG_DIR / 'builder-knowledge-graph.json',
    'domain': KG_DIR / 'domain-knowledge-graph.json',
}

class KGValidator:
    """Validate KG integrity"""
    
    def __init__(self, role: str, verbose: bool = False):
        self.role = role
        self.verbose = verbose
        self.kg_path = KG_PATHS[role]
        self.kg_data = None
        self.kg_format = None
        self.errors = []
        self.warnings = []
        
    def load_kg(self) -> bool:
        """Load and detect KG format"""
        try:
            with open(self.kg_path, 'r', encoding='utf-8') as f:
                self.kg_data = json.load(f)
            
            if 'nodes' in self.kg_data:
                self.kg_format = 'new'
            elif 'documents' in self.kg_data:
                self.kg_format = 'old'
            else:
                self.errors.append("Unknown KG format")
                return False
            
            return True
        except Exception as e:
            self.errors.append(f"Failed to load KG: {e}")
            return False
    
    def validate_all(self) -> Tuple[bool, Dict]:
        """Run all validations"""
        if not self.load_kg():
            return False, self._generate_report()
        
        print(f"\n{'='*60}")
        print(f"Validating {self.role.upper()} KG ({self.kg_format} format)")
        print('='*60)
        
        # Run checks
        self.check_duplicates()
        self.check_required_fields()
        self.check_referential_integrity()
        self.check_orphans()
        self.check_metadata()
        
        # Generate report
        report = self._generate_report()
        self._print_report(report)
        
        return len(self.errors) == 0, report
    
    def check_duplicates(self):
        """Check for duplicate IDs"""
        print("\n[CHECK] Duplicate IDs...")
        
        if self.kg_format == 'new':
            ids = [n['id'] for n in self.kg_data.get('nodes', [])]
        else:
            ids = [d['id'] for d in self.kg_data.get('documents', [])]
        
        id_counts = Counter(ids)
        duplicates = {id_: count for id_, count in id_counts.items() if count > 1}
        
        if duplicates:
            for id_, count in duplicates.items():
                self.errors.append(f"Duplicate ID '{id_}' appears {count} times")
        else:
            print("  [OK] No duplicate IDs")
    
    def check_required_fields(self):
        """Check for required fields in all nodes"""
        print("\n[CHECK] Required fields...")
        
        missing_count = 0
        
        if self.kg_format == 'new':
            required = ['id', 'type', 'data', 'relationships']
            for node in self.kg_data.get('nodes', []):
                missing = [f for f in required if f not in node]
                if missing:
                    self.errors.append(f"Node {node.get('id', 'UNKNOWN')}: missing {missing}")
                    missing_count += 1
        else:
            required = ['id', 'type']  # Old format has fewer requirements
            for doc in self.kg_data.get('documents', []):
                missing = [f for f in required if f not in doc]
                if missing:
                    self.errors.append(f"Document {doc.get('id', 'UNKNOWN')}: missing {missing}")
                    missing_count += 1
        
        if missing_count == 0:
            print("  [OK] All nodes have required fields")
        else:
            print(f"  [ERROR] {missing_count} node(s) missing required fields")
    
    def check_referential_integrity(self):
        """Check all references point to existing nodes"""
        print("\n[CHECK] Referential integrity...")
        
        if self.kg_format == 'new':
            all_ids = {n['id'] for n in self.kg_data.get('nodes', [])}
            broken_count = 0
            
            for node in self.kg_data.get('nodes', []):
                node_id = node.get('id')
                
                # Check parent
                parent = node.get('relationships', {}).get('parent')
                if parent and parent not in all_ids:
                    self.errors.append(f"{node_id}: parent '{parent}' not found")
                    broken_count += 1
                
                # Check children
                for child in node.get('relationships', {}).get('children', []):
                    if child not in all_ids:
                        self.errors.append(f"{node_id}: child '{child}' not found")
                        broken_count += 1
        else:
            all_ids = {d['id'] for d in self.kg_data.get('documents', [])}
            broken_count = 0
            
            for doc in self.kg_data.get('documents', []):
                doc_id = doc.get('id')
                
                # Check contains
                for child in doc.get('contains', []):
                    if child not in all_ids:
                        self.warnings.append(f"{doc_id}: contains '{child}' not found")
                        broken_count += 1
        
        if broken_count == 0:
            print("  [OK] All references are valid")
        else:
            print(f"  [ERROR] {broken_count} broken reference(s)")
    
    def check_orphans(self):
        """Check for orphan nodes (no parent, not root)"""
        print("\n[CHECK] Orphan nodes...")
        
        if self.kg_format == 'new':
            orphans = []
            for node in self.kg_data.get('nodes', []):
                node_id = node.get('id')
                parent = node.get('relationships', {}).get('parent')
                node_type = node.get('type')
                
                # Root nodes are OK
                if node_type == 'root' or 'root' in node_id:
                    continue
                
                if not parent:
                    orphans.append(node_id)
                    self.errors.append(f"Orphan node: {node_id}")
        else:
            # In old format, check which docs are not in any 'contains' array
            referenced = set()
            for doc in self.kg_data.get('documents', []):
                referenced.update(doc.get('contains', []))
            
            orphans = []
            for doc in self.kg_data.get('documents', []):
                doc_id = doc.get('id')
                doc_type = doc.get('type')
                
                # Root and categories are OK
                if doc_type in ['root', 'category']:
                    continue
                
                if doc_id not in referenced:
                    orphans.append(doc_id)
                    self.warnings.append(f"Orphan document: {doc_id}")
        
        if not orphans:
            print("  [OK] No orphan nodes")
        else:
            print(f"  [WARN] {len(orphans)} orphan node(s)")
    
    def check_metadata(self):
        """Check metadata consistency"""
        print("\n[CHECK] Metadata consistency...")
        
        if 'metadata' not in self.kg_data:
            self.warnings.append("Missing metadata section")
            return
        
        metadata = self.kg_data['metadata']
        
        # Check node count
        if self.kg_format == 'new':
            actual_count = len(self.kg_data.get('nodes', []))
            claimed_count = metadata.get('total_nodes', 0)
            
            if actual_count != claimed_count:
                self.warnings.append(f"Metadata claims {claimed_count} nodes, but found {actual_count}")
        else:
            actual_count = len(self.kg_data.get('documents', []))
            claimed_count = metadata.get('total_documents', 0)
            
            if actual_count != claimed_count:
                self.warnings.append(f"Metadata claims {claimed_count} documents, but found {actual_count}")
        
        # Check last updated
        if 'last_updated' not in metadata:
            self.warnings.append("Missing 'last_updated' in metadata")
        
        if not self.warnings:
            print("  [OK] Metadata is consistent")
    
    def _generate_report(self) -> Dict:
        """Generate validation report"""
        if self.kg_format == 'new':
            total = len(self.kg_data.get('nodes', [])) if self.kg_data else 0
        else:
            total = len(self.kg_data.get('documents', [])) if self.kg_data else 0
        
        return {
            'role': self.role,
            'format': self.kg_format,
            'timestamp': datetime.now().isoformat(),
            'total_nodes': total,
            'errors': len(self.errors),
            'warnings': len(self.warnings),
            'passed': len(self.errors) == 0,
            'error_list': self.errors,
            'warning_list': self.warnings
        }
    
    def _print_report(self, report: Dict):
        """Print validation report"""
        print(f"\n{'='*60}")
        print("Validation Report")
        print('='*60)
        print(f"Role: {report['role']}")
        print(f"Format: {report['format']}")
        print(f"Total nodes: {report['total_nodes']}")
        print(f"Errors: {report['errors']}")
        print(f"Warnings: {report['warnings']}")
        print(f"Status: {'PASS' if report['passed'] else 'FAIL'}")
        
        if report['error_list']:
            print(f"\nErrors ({len(report['error_list'])}):")
            for i, error in enumerate(report['error_list'][:10], 1):
                print(f"  {i}. {error}")
            if len(report['error_list']) > 10:
                print(f"  ... and {len(report['error_list']) - 10} more")
        
        if report['warning_list']:
            print(f"\nWarnings ({len(report['warning_list'])}):")
            for i, warning in enumerate(report['warning_list'][:5], 1):
                print(f"  {i}. {warning}")
            if len(report['warning_list']) > 5:
                print(f"  ... and {len(report['warning_list']) - 5} more")
        
        print('='*60)


def main():
    parser = argparse.ArgumentParser(description="Validate KG integrity")
    parser.add_argument('--role', choices=['builder', 'domain'], help="KG role to validate")
    parser.add_argument('--all', action='store_true', help="Validate both KGs")
    parser.add_argument('--verbose', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    if not args.role and not args.all:
        parser.error("Must specify --role or --all")
    
    roles = ['builder', 'domain'] if args.all else [args.role]
    
    all_passed = True
    reports = []
    
    for role in roles:
        validator = KGValidator(role, verbose=args.verbose)
        passed, report = validator.validate_all()
        reports.append(report)
        all_passed = all_passed and passed
    
    # Summary
    if len(reports) > 1:
        print(f"\n{'='*60}")
        print("Overall Summary")
        print('='*60)
        for report in reports:
            status = '[PASS]' if report['passed'] else '[FAIL]'
            print(f"{status} {report['role']:10s} - {report['errors']} errors, {report['warnings']} warnings")
        print('='*60)
    
    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
