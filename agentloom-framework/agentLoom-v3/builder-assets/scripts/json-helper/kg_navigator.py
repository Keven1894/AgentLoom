#!/usr/bin/env python3
"""
KG Navigator - Helper for traversing Knowledge Graph relationships

Makes it easy for LLMs to navigate KG structure without manual JSON parsing.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set


class KGNavigator:
    """Navigate Knowledge Graph relationships"""
    
    def __init__(self, kg_file: Path):
        """
        Initialize navigator
        
        Args:
            kg_file: Path to KG JSON file
        """
        self.kg_file = Path(kg_file)
        self.data = None
        self.nodes = []
        self.node_index = {}  # id -> node mapping
        
    def load(self) -> bool:
        """Load KG file"""
        try:
            with open(self.kg_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            
            # Determine node array name
            graph_type = self.data.get('graphType')
            if graph_type == 'skills':
                self.nodes = self.data.get('skills', [])
            elif graph_type == 'behaviors':
                self.nodes = self.data.get('behaviors', [])
            elif graph_type in ['knowledge', 'project-graph']:
                self.nodes = self.data.get('nodes', [])
            else:
                self.nodes = []
            
            # Build index
            self.node_index = {node['id']: node for node in self.nodes}
            
            print(f"✓ Loaded {len(self.nodes)} nodes from {self.kg_file.name}")
            return True
        
        except Exception as e:
            print(f"❌ Failed to load: {e}")
            return False
    
    def get_node(self, node_id: str) -> Optional[Dict]:
        """Get node by ID"""
        return self.node_index.get(node_id)
    
    def get_links(self, node_id: str, link_type: Optional[str] = None) -> Dict[str, List[str]]:
        """
        Get all links from a node
        
        Args:
            node_id: Source node ID
            link_type: Optional filter by link type
        
        Returns:
            Dict of link_type -> [target_ids]
        """
        node = self.get_node(node_id)
        if not node:
            return {}
        
        links = node.get('links', {})
        
        if link_type:
            return {link_type: links.get(link_type, [])}
        
        return links
    
    def get_linked_nodes(self, node_id: str, link_type: str) -> List[Dict]:
        """
        Get all nodes linked via specific link type
        
        Args:
            node_id: Source node ID
            link_type: Link type (e.g., 'uses', 'references')
        
        Returns:
            List of linked nodes
        """
        links = self.get_links(node_id, link_type)
        target_ids = links.get(link_type, [])
        
        nodes = []
        for target_id in target_ids:
            target_node = self.get_node(target_id)
            if target_node:
                nodes.append(target_node)
        
        return nodes
    
    def traverse(self, start_id: str, link_types: List[str], 
                 max_depth: int = 3) -> Dict[str, Set[str]]:
        """
        Traverse KG from starting node following link types
        
        Args:
            start_id: Starting node ID
            link_types: Link types to follow
            max_depth: Maximum traversal depth
        
        Returns:
            Dict of node_type -> set of node IDs found
        """
        visited = set()
        found = {}
        
        def _traverse(node_id: str, depth: int):
            if depth > max_depth or node_id in visited:
                return
            
            visited.add(node_id)
            node = self.get_node(node_id)
            
            if not node:
                return
            
            # Categorize by type
            node_type = node.get('type', 'unknown')
            if node_type not in found:
                found[node_type] = set()
            found[node_type].add(node_id)
            
            # Follow links
            for link_type in link_types:
                targets = self.get_links(node_id, link_type).get(link_type, [])
                for target_id in targets:
                    _traverse(target_id, depth + 1)
        
        _traverse(start_id, 0)
        return found
    
    def find_by_type(self, node_type: str) -> List[Dict]:
        """Find all nodes of specific type"""
        return [n for n in self.nodes if n.get('type') == node_type]
    
    def find_by_path(self, path_pattern: str) -> List[Dict]:
        """Find nodes matching path pattern"""
        return [n for n in self.nodes if path_pattern in n.get('path', '')]
    
    def get_dependencies(self, node_id: str) -> Dict[str, List[str]]:
        """
        Get all dependencies of a node
        
        Returns:
            Dict categorizing dependencies by type
        """
        deps = {
            'skills': [],
            'behaviors': [],
            'documents': [],
            'scripts': [],
            'other': []
        }
        
        # Common dependency link types
        dep_links = ['uses', 'depends_on', 'references', 'governed_by', 
                     'implements', 'extends']
        
        for link_type in dep_links:
            linked = self.get_linked_nodes(node_id, link_type)
            for node in linked:
                node_id = node['id']
                
                if node_id.startswith('skill'):
                    deps['skills'].append(node_id)
                elif node_id.startswith('behavior'):
                    deps['behaviors'].append(node_id)
                elif node_id.startswith('docs'):
                    deps['documents'].append(node_id)
                elif 'script' in node.get('path', ''):
                    deps['scripts'].append(node_id)
                else:
                    deps['other'].append(node_id)
        
        return deps
    
    def print_node(self, node_id: str, show_links: bool = True):
        """Pretty print node details"""
        node = self.get_node(node_id)
        if not node:
            print(f"❌ Node not found: {node_id}")
            return
        
        print(f"\n{'='*60}")
        print(f"Node: {node_id}")
        print(f"{'='*60}")
        print(f"Type: {node.get('type', 'N/A')}")
        print(f"Name: {node.get('name', node.get('title', 'N/A'))}")
        print(f"Path: {node.get('path', 'N/A')}")
        
        if 'description' in node:
            print(f"Description: {node['description'][:100]}...")
        
        if show_links and 'links' in node:
            print(f"\nLinks:")
            for link_type, targets in node['links'].items():
                print(f"  {link_type}: {len(targets)} targets")
                for target in targets[:3]:  # Show first 3
                    print(f"    - {target}")
                if len(targets) > 3:
                    print(f"    ... and {len(targets) - 3} more")


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Navigate Knowledge Graphs')
    parser.add_argument('kg_file', help='Path to KG JSON file')
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Get node command
    get_cmd = subparsers.add_parser('get', help='Get node by ID')
    get_cmd.add_argument('node_id', help='Node ID')
    
    # Find command
    find_cmd = subparsers.add_parser('find', help='Find nodes')
    find_cmd.add_argument('--type', help='Node type')
    find_cmd.add_argument('--path', help='Path pattern')
    
    # Dependencies command
    deps_cmd = subparsers.add_parser('deps', help='Get dependencies')
    deps_cmd.add_argument('node_id', help='Node ID')
    
    # Traverse command
    trav_cmd = subparsers.add_parser('traverse', help='Traverse from node')
    trav_cmd.add_argument('node_id', help='Starting node ID')
    trav_cmd.add_argument('--links', nargs='+', default=['uses', 'references'],
                          help='Link types to follow')
    trav_cmd.add_argument('--depth', type=int, default=3, help='Max depth')
    
    args = parser.parse_args()
    
    nav = KGNavigator(args.kg_file)
    if not nav.load():
        exit(1)
    
    if args.command == 'get':
        nav.print_node(args.node_id)
    
    elif args.command == 'find':
        if args.type:
            nodes = nav.find_by_type(args.type)
            print(f"Found {len(nodes)} nodes of type '{args.type}':")
            for node in nodes[:10]:
                print(f"  - {node['id']}")
        elif args.path:
            nodes = nav.find_by_path(args.path)
            print(f"Found {len(nodes)} nodes matching path '{args.path}':")
            for node in nodes[:10]:
                print(f"  - {node['id']}: {node.get('path')}")
    
    elif args.command == 'deps':
        deps = nav.get_dependencies(args.node_id)
        print(f"\nDependencies of {args.node_id}:")
        for dep_type, dep_list in deps.items():
            if dep_list:
                print(f"\n{dep_type.upper()}:")
                for dep in dep_list:
                    print(f"  - {dep}")
    
    elif args.command == 'traverse':
        result = nav.traverse(args.node_id, args.links, args.depth)
        print(f"\nTraversed from {args.node_id}:")
        for node_type, node_ids in result.items():
            print(f"\n{node_type}: {len(node_ids)} nodes")
            for nid in list(node_ids)[:5]:
                print(f"  - {nid}")


if __name__ == '__main__':
    main()
