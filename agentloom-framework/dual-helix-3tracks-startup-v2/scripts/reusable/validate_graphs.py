#!/usr/bin/env python3
"""
Knowledge Graph Validator (V2.0)
Validates graph connectivity and structure

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
    
    # Handle different graph formats
    nodes = graph.get('nodes', []) or graph.get('skills', []) or graph.get('behaviors', [])
    all_ids = {node['id'] for node in nodes}
    
    issues = []
    
    for node in nodes:
        node_id = node.get('id')
        node_type = node.get('type', '')
        
        # Check orphaned nodes (non-root without parent)
        if node_type != 'root' and 'parent' not in node:
            issues.append({
                'type': 'orphaned',
                'node': node_id,
                'graph': graph_path.name,
                'message': f"Node '{node_id}' has no parent field"
            })
        
        # Check broken parent references
        if 'parent' in node and node['parent'] not in all_ids:
            issues.append({
                'type': 'broken_parent',
                'node': node_id,
                'invalid_parent': node['parent'],
                'graph': graph_path.name,
                'message': f"Node '{node_id}' references non-existent parent '{node['parent']}'"
            })
        
        # Check broken cross-graph links
        if 'links' in node:
            for link in node['links']:
                # Cross-graph links are OK (can't validate here)
                # Just check format
                if not isinstance(link, dict) or 'target' not in link:
                    issues.append({
                        'type': 'invalid_link',
                        'node': node_id,
                        'graph': graph_path.name,
                        'message': f"Node '{node_id}' has malformed link"
                    })
    
    return issues


def validate_graph_structure(graph_path):
    """Validate basic graph structure"""
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph = json.load(f)
    
    issues = []
    
    # Check for nodes array
    nodes = graph.get('nodes', []) or graph.get('skills', []) or graph.get('behaviors', [])
    if not nodes:
        issues.append({
            'type': 'empty_graph',
            'graph': graph_path.name,
            'message': f"Graph '{graph_path.name}' has no nodes"
        })
        return issues
    
    # Check for root node
    root_nodes = [n for n in nodes if n.get('type') == 'root']
    if not root_nodes:
        issues.append({
            'type': 'no_root',
            'graph': graph_path.name,
            'message': f"Graph '{graph_path.name}' has no root node"
        })
    elif len(root_nodes) > 1:
        issues.append({
            'type': 'multiple_roots',
            'graph': graph_path.name,
            'message': f"Graph '{graph_path.name}' has {len(root_nodes)} root nodes (should have 1)"
        })
    
    return issues


def main():
    """Scan all graphs for issues"""
    graphs_dir = Path('agents/knowledge-graphs')
    
    if not graphs_dir.exists():
        print(f"❌ Error: Directory '{graphs_dir}' not found")
        return 1
    
    graph_files = list(graphs_dir.glob('*.json'))
    if not graph_files:
        print(f"❌ Error: No JSON files found in '{graphs_dir}'")
        return 1
    
    all_issues = []
    
    print(f"Validating {len(graph_files)} knowledge graphs...")
    print("=" * 60)
    
    for graph_file in sorted(graph_files):
        print(f"\nChecking {graph_file.name}...")
        
        # Validate structure
        structure_issues = validate_graph_structure(graph_file)
        all_issues.extend(structure_issues)
        
        # Validate connectivity
        connectivity_issues = check_connectivity(graph_file)
        all_issues.extend(connectivity_issues)
        
        if not structure_issues and not connectivity_issues:
            print(f"  ✅ Valid")
    
    print("\n" + "=" * 60)
    
    if all_issues:
        print(f"\n❌ Found {len(all_issues)} issues:\n")
        
        # Group by type
        by_type = {}
        for issue in all_issues:
            issue_type = issue['type']
            if issue_type not in by_type:
                by_type[issue_type] = []
            by_type[issue_type].append(issue)
        
        for issue_type, issues in by_type.items():
            print(f"\n{issue_type.upper().replace('_', ' ')} ({len(issues)}):")
            for issue in issues:
                print(f"  - {issue['message']}")
        
        return 1
    else:
        print(f"\n✅ All {len(graph_files)} graphs are fully connected and valid!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
