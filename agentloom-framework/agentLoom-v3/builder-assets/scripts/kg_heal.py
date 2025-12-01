#!/usr/bin/env python3
"""
KG Heal - Graph Connectivity Validator
Validates graph connectivity and reports issues

This script is 100% reusable across all agent projects.
No customization needed.
"""

import json
import sys
from pathlib import Path


def check_connectivity(graph_path):
    """Check for orphaned nodes and broken references"""
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph = json.load(f)
    
    nodes = graph.get('nodes', []) or graph.get('skills', []) or graph.get('behaviors', [])
    all_ids = {node['id'] for node in nodes}
    
    issues = []
    
    for node in nodes:
        node_id = node.get('id')
        node_type = node.get('type', '')
        
        # Check orphaned nodes
        if node_type != 'root' and 'parent' not in node:
            issues.append({
                'type': 'orphaned',
                'node': node_id,
                'graph': str(graph_path)
            })
        
        # Check broken parent references
        if 'parent' in node and node['parent'] not in all_ids:
            issues.append({
                'type': 'broken_parent',
                'node': node_id,
                'invalid_parent': node['parent'],
                'graph': str(graph_path)
            })
    
    return issues


def main():
    """Scan all graphs for connectivity issues"""
    graphs_dir = Path('agents/knowledge-graphs')
    
    if not graphs_dir.exists():
        print(f"❌ Error: Directory '{graphs_dir}' not found")
        return 1
    
    all_issues = []
    
    for graph_file in graphs_dir.glob('*.json'):
        issues = check_connectivity(graph_file)
        all_issues.extend(issues)
    
    if all_issues:
        print(f"⚠️  Found {len(all_issues)} connectivity issues:")
        for issue in all_issues:
            print(f"  - {issue['type']}: {issue['node']} in {issue['graph']}")
        return 1
    else:
        print("✅ All graphs are fully connected!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
