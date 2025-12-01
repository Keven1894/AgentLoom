import json
import os
import sys
from pathlib import Path

def validate_graph(graph_path):
    """Validates JSON graph structure and file references"""
    print(f"\n🔍 Validating {graph_path}...")
    
    try:
        with open(graph_path, 'r', encoding='utf-8') as f:
            graph = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {graph_path}")
        return False
    
    # Check required fields based on graph type
    required_fields = {
        'master': ['graphType', 'project', 'graphs', 'roles'],
        'knowledge': ['graphType', 'role', 'nodes'],
        'skills': ['graphType', 'role', 'skills'],
        'behaviors': ['graphType', 'role', 'behaviors'],
        'project-graph': ['graphType', 'nodes']
    }
    
    graph_type = graph.get('graphType', 'unknown')
    required = required_fields.get(graph_type, ['graphType'])
    
    for field in required:
        if field not in graph:
            print(f"❌ Missing required field: {field}")
            return False
    
    # Validate file references
    files_checked = 0
    files_missing = 0
    
    # Check nodes (Knowledge Graphs)
    if 'nodes' in graph:
        for node in graph['nodes']:
            if 'path' in node:
                files_checked += 1
                if not os.path.exists(node['path']):
                    print(f"⚠️  Missing file: {node['path']} (Node: {node.get('title', 'unknown')})")
                    files_missing += 1
    
    # Check skills
    if 'skills' in graph:
        for skill in graph['skills']:
            if 'path' in skill:
                files_checked += 1
                if not os.path.exists(skill['path']):
                    print(f"⚠️  Missing file: {skill['path']} (Skill: {skill.get('name', 'unknown')})")
                    files_missing += 1

    # Check behaviors
    if 'behaviors' in graph:
        for behavior in graph['behaviors']:
            if 'path' in behavior:
                files_checked += 1
                if not os.path.exists(behavior['path']):
                    print(f"⚠️  Missing file: {behavior['path']} (Behavior: {behavior.get('name', 'unknown')})")
                    files_missing += 1
                    
    # Check master graph links
    if 'graphs' in graph:
        for sub_graph in graph['graphs']:
            if 'path' in sub_graph:
                files_checked += 1
                if not os.path.exists(sub_graph['path']):
                    print(f"⚠️  Missing graph file: {sub_graph['path']}")
                    files_missing += 1

    if files_missing > 0:
        print(f"⚠️  {files_missing}/{files_checked} referenced files missing")
    else:
        print(f"✅ All {files_checked} referenced files exist")
    
    print(f"✅ {os.path.basename(graph_path)} structure is valid")
    return True

def main():
    print("=" * 60)
    print("Knowledge Graph Validation")
    print("=" * 60)
    
    graphs_dir = Path('agents/knowledge-graphs')
    if not graphs_dir.exists():
        print("❌ knowledge-graphs directory not found!")
        return False
    
    graphs = list(graphs_dir.glob('*.json'))
    if not graphs:
        print("❌ No graph files found!")
        return False
    
    results = []
    for graph_path in graphs:
        results.append(validate_graph(str(graph_path)))
    
    print("\n" + "=" * 60)
    success_count = sum(results)
    total_count = len(results)
    print(f"Validation Complete: {success_count}/{total_count} graphs valid")
    print("=" * 60)
    
    return success_count == total_count

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

