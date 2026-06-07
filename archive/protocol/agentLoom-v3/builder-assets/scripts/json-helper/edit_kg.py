#!/usr/bin/env python3
"""
JSON Knowledge Graph Editor

A rule-based tool for safely manipulating JSON knowledge graph files.
Designed to be invoked by LLMs without risk of JSON corruption.

Usage:
    # Add a new node
    python scripts/edit_kg.py add --file agents/knowledge-graphs/manager-skills-graph.json --node skill-new-skill --data '{"id": "skill-new-skill", "name": "New Skill", ...}'
    
    # Update existing node
    python scripts/edit_kg.py update --file agents/knowledge-graphs/manager-skills-graph.json --node skill-existing --field description --value "Updated description"
    
    # Remove a node
    python scripts/edit_kg.py remove --file agents/knowledge-graphs/manager-skills-graph.json --node skill-old-skill
    
    # Add link between nodes
    python scripts/edit_kg.py link --file agents/knowledge-graphs/manager-skills-graph.json --from skill-a --to skill-b --link-type uses
    
    # Validate JSON structure
    python scripts/edit_kg.py validate --file agents/knowledge-graphs/manager-skills-graph.json
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import shutil

class KGEditor:
    """Safe JSON Knowledge Graph Editor"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.data = None
        self.backup_path = None
        
    def load(self) -> bool:
        """Load JSON file"""
        if not self.file_path.exists():
            print(f"❌ File not found: {self.file_path}")
            return False
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"✓ Loaded {self.file_path}")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return False
    
    def backup(self):
        """Create backup before modification"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_path = self.file_path.with_suffix(f'.backup_{timestamp}.json')
        shutil.copy2(self.file_path, self.backup_path)
        print(f"✓ Backup created: {self.backup_path}")
    
    def save(self, validate: bool = True) -> bool:
        """Save JSON file with validation"""
        if validate and not self.validate():
            print("❌ Validation failed, not saving")
            return False
        
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved {self.file_path}")
            return True
        except Exception as e:
            print(f"❌ Save failed: {e}")
            if self.backup_path:
                print(f"   Restore from: {self.backup_path}")
            return False
    
    def validate(self) -> bool:
        """Validate JSON structure"""
        try:
            # Check if it's valid JSON
            json.dumps(self.data)
            
            # Check required fields based on graph type
            if 'graphType' not in self.data:
                print("❌ Missing 'graphType' field")
                return False
            
            graph_type = self.data['graphType']
            
            # Type-specific validation
            if graph_type == 'skills':
                if 'skills' not in self.data:
                    print("❌ Missing 'skills' array")
                    return False
                if not isinstance(self.data['skills'], list):
                    print("❌ 'skills' must be an array")
                    return False
            
            elif graph_type == 'behaviors':
                if 'behaviors' not in self.data:
                    print("❌ Missing 'behaviors' array")
                    return False
            
            elif graph_type == 'knowledge':
                if 'nodes' not in self.data:
                    print("❌ Missing 'nodes' array")
                    return False
            
            elif graph_type == 'project-graph':
                if 'nodes' not in self.data:
                    print("❌ Missing 'nodes' array")
                    return False
            
            print("✓ Validation passed")
            return True
            
        except Exception as e:
            print(f"❌ Validation error: {e}")
            return False
    
    def find_node(self, node_id: str) -> Optional[Dict]:
        """Find a node by ID"""
        # Determine the array name based on graph type
        graph_type = self.data.get('graphType')
        
        if graph_type == 'skills':
            array_name = 'skills'
        elif graph_type == 'behaviors':
            array_name = 'behaviors'
        elif graph_type in ['knowledge', 'project-graph']:
            array_name = 'nodes'
        else:
            print(f"❌ Unknown graph type: {graph_type}")
            return None
        
        nodes = self.data.get(array_name, [])
        for node in nodes:
            if node.get('id') == node_id:
                return node
        
        return None
    
    def add_node(self, node_data: Dict) -> bool:
        """Add a new node"""
        node_id = node_data.get('id')
        if not node_id:
            print("❌ Node must have 'id' field")
            return False
        
        # Check if node already exists
        if self.find_node(node_id):
            print(f"❌ Node '{node_id}' already exists")
            return False
        
        # Determine array name
        graph_type = self.data.get('graphType')
        if graph_type == 'skills':
            array_name = 'skills'
        elif graph_type == 'behaviors':
            array_name = 'behaviors'
        elif graph_type in ['knowledge', 'project-graph']:
            array_name = 'nodes'
        else:
            print(f"❌ Unknown graph type: {graph_type}")
            return False
        
        # Add node
        self.data[array_name].append(node_data)
        print(f"✓ Added node: {node_id}")
        return True
    
    def update_node(self, node_id: str, field: str, value: Any) -> bool:
        """Update a field in an existing node"""
        node = self.find_node(node_id)
        if not node:
            print(f"❌ Node '{node_id}' not found")
            return False
        
        node[field] = value
        print(f"✓ Updated {node_id}.{field}")
        return True
    
    def remove_node(self, node_id: str) -> bool:
        """Remove a node"""
        graph_type = self.data.get('graphType')
        
        if graph_type == 'skills':
            array_name = 'skills'
        elif graph_type == 'behaviors':
            array_name = 'behaviors'
        elif graph_type in ['knowledge', 'project-graph']:
            array_name = 'nodes'
        else:
            print(f"❌ Unknown graph type: {graph_type}")
            return False
        
        nodes = self.data[array_name]
        original_len = len(nodes)
        self.data[array_name] = [n for n in nodes if n.get('id') != node_id]
        
        if len(self.data[array_name]) == original_len:
            print(f"❌ Node '{node_id}' not found")
            return False
        
        print(f"✓ Removed node: {node_id}")
        return True
    
    def add_link(self, from_id: str, to_id: str, link_type: str) -> bool:
        """Add a link between nodes"""
        node = self.find_node(from_id)
        if not node:
            print(f"❌ Node '{from_id}' not found")
            return False
        
        # Initialize links if not present
        if 'links' not in node:
            node['links'] = {}
        
        # Initialize link type array if not present
        if link_type not in node['links']:
            node['links'][link_type] = []
        
        # Add link if not already present
        if to_id not in node['links'][link_type]:
            node['links'][link_type].append(to_id)
            print(f"✓ Added link: {from_id} --{link_type}--> {to_id}")
            return True
        else:
            print(f"⚠️  Link already exists: {from_id} --{link_type}--> {to_id}")
            return True
    
    def remove_link(self, from_id: str, to_id: str, link_type: str) -> bool:
        """Remove a link between nodes"""
        node = self.find_node(from_id)
        if not node:
            print(f"❌ Node '{from_id}' not found")
            return False
        
        if 'links' not in node or link_type not in node['links']:
            print(f"❌ No '{link_type}' links found")
            return False
        
        if to_id in node['links'][link_type]:
            node['links'][link_type].remove(to_id)
            print(f"✓ Removed link: {from_id} --{link_type}--> {to_id}")
            return True
        else:
            print(f"❌ Link not found: {from_id} --{link_type}--> {to_id}")
            return False


def main():
    parser = argparse.ArgumentParser(description='Safe JSON Knowledge Graph Editor')
    parser.add_argument('action', choices=['add', 'update', 'remove', 'link', 'unlink', 'validate'],
                       help='Action to perform')
    parser.add_argument('--file', required=True, help='Path to JSON file')
    parser.add_argument('--node', help='Node ID')
    parser.add_argument('--data', help='JSON data for new node (for add action)')
    parser.add_argument('--data-file', help='Path to JSON file containing node data (for add action)')
    parser.add_argument('--field', help='Field name (for update action)')
    parser.add_argument('--value', help='Field value (for update action)')
    parser.add_argument('--from', dest='from_node', help='Source node ID (for link/unlink)')
    parser.add_argument('--to', dest='to_node', help='Target node ID (for link/unlink)')
    parser.add_argument('--link-type', help='Link type (for link/unlink)')
    parser.add_argument('--no-backup', action='store_true', help='Skip backup creation')
    
    args = parser.parse_args()
    
    # Initialize editor
    editor = KGEditor(args.file)
    
    # Load file
    if not editor.load():
        sys.exit(1)
    
    # Create backup (unless disabled or validating)
    if not args.no_backup and args.action != 'validate':
        editor.backup()
    
    # Perform action
    success = False
    
    if args.action == 'add':
        if not args.data and not args.data_file:
            print("❌ --data or --data-file required for add action")
            sys.exit(1)
        try:
            if args.data_file:
                with open(args.data_file, 'r', encoding='utf-8') as f:
                    node_data = json.load(f)
            else:
                node_data = json.loads(args.data)
            success = editor.add_node(node_data)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON data: {e}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"❌ Data file not found: {args.data_file}")
            sys.exit(1)
    
    elif args.action == 'update':
        if not args.node or not args.field:
            print("❌ --node and --field required for update action")
            sys.exit(1)
        # Try to parse value as JSON, otherwise use as string
        try:
            value = json.loads(args.value)
        except:
            value = args.value
        success = editor.update_node(args.node, args.field, value)
    
    elif args.action == 'remove':
        if not args.node:
            print("❌ --node required for remove action")
            sys.exit(1)
        success = editor.remove_node(args.node)
    
    elif args.action == 'link':
        if not args.from_node or not args.to_node or not args.link_type:
            print("❌ --from, --to, and --link-type required for link action")
            sys.exit(1)
        success = editor.add_link(args.from_node, args.to_node, args.link_type)
    
    elif args.action == 'unlink':
        if not args.from_node or not args.to_node or not args.link_type:
            print("❌ --from, --to, and --link-type required for unlink action")
            sys.exit(1)
        success = editor.remove_link(args.from_node, args.to_node, args.link_type)
    
    elif args.action == 'validate':
        success = editor.validate()
        sys.exit(0 if success else 1)
    
    # Save if action succeeded
    if success:
        if editor.save():
            print(f"\n✅ Success! File updated: {args.file}")
            sys.exit(0)
        else:
            print(f"\n❌ Failed to save file")
            sys.exit(1)
    else:
        print(f"\n❌ Action failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
