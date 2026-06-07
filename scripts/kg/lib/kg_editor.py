#!/usr/bin/env python3
"""
JSON Knowledge Graph Editor

High-level wrapper combining validator, updater, and generator
for convenient KG operations.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Union

# Handle both module and standalone script usage
try:
    from .validator import KGValidator, ValidationResult
    from .updater import KGUpdater, UpdateResult
    from .generator import NodeGenerator
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from validator import KGValidator, ValidationResult
    from updater import KGUpdater, UpdateResult
    from generator import NodeGenerator


class KGEditor:
    """
    High-level Knowledge Graph Editor
    
    Combines validator, updater, and generator for convenient operations.
    """
    
    def __init__(self, file_path: Union[str, Path], 
                 auto_backup: bool = True,
                 auto_validate: bool = True):
        """
        Initialize KG Editor
        
        Args:
            file_path: Path to JSON KG file
            auto_backup: Automatically backup before changes
            auto_validate: Automatically validate before/after changes
        """
        self.file_path = Path(file_path)
        self.validator = KGValidator()
        self.updater = KGUpdater(file_path, auto_backup, auto_validate)
        self.generator = NodeGenerator()
        self.loaded = False
    
    def load(self) -> bool:
        """Load KG file"""
        self.loaded = self.updater.load()
        return self.loaded
    
    def validate(self) -> ValidationResult:
        """Validate current data"""
        if not self.loaded:
            return ValidationResult(False, ["File not loaded"], [])
        return self.updater.validate()
    
    def save(self) -> UpdateResult:
        """Save changes to file"""
        return self.updater.save()
    
    def rollback(self) -> UpdateResult:
        """Rollback to original state"""
        return self.updater.rollback()
    
    # High-level operations
    
    def add_skill(self, id: str, name: str, category: str,
                  description: str = '', path: str = '',
                  parent: str = 'skill:manager:root',
                  links: Optional[Dict] = None) -> UpdateResult:
        """
        Add a skill node
        
        Args:
            id: Skill ID
            name: Skill name
            category: Skill category
            description: Description
            path: Path to markdown file
            parent: Parent skill ID
            links: Links dict
        
        Returns:
            UpdateResult
        """
        if not self.loaded:
            return UpdateResult(False, "File not loaded")
        
        # Generate skill node
        skill = self.generator.create_skill(
            id=id,
            name=name,
            category=category,
            description=description,
            path=path,
            parent=parent
        )
        
        if links:
            skill['links'] = links
        
        # Add to graph
        return self.updater.add_node(skill)
    
    def add_project(self, id: str, category: str, path: str,
                   title: str, description: str = '',
                   status: str = 'active') -> UpdateResult:
        """
        Add a project node
        
        Args:
            id: Project ID (with category prefix)
            category: Category
            path: Project path
            title: Project title
            description: Description
            status: Status
        
        Returns:
            UpdateResult
        """
        if not self.loaded:
            return UpdateResult(False, "File not loaded")
        
        project = self.generator.create_project(
            id=id,
            category=category,
            path=path,
            title=title,
            description=description,
            status=status
        )
        
        return self.updater.add_node(project)
    
    def add_document(self, id: str, path: str, title: str,
                    parent: str) -> UpdateResult:
        """
        Add a document node
        
        Args:
            id: Document ID
            path: Document path
            title: Document title
            parent: Parent project ID
        
        Returns:
            UpdateResult
        """
        if not self.loaded:
            return UpdateResult(False, "File not loaded")
        
        document = self.generator.create_document(
            id=id,
            path=path,
            title=title,
            parent=parent
        )
        
        return self.updater.add_node(document)
    
    def update_field(self, node_id: str, field: str, value: any) -> UpdateResult:
        """
        Update a field in a node
        
        Args:
            node_id: Node ID
            field: Field name
            value: New value
        
        Returns:
            UpdateResult
        """
        if not self.loaded:
            return UpdateResult(False, "File not loaded")
        
        return self.updater.update_node_field(node_id, field, value)
    
    def add_link(self, from_id: str, to_id: str, link_type: str) -> UpdateResult:
        """
        Add a link between nodes
        
        Args:
            from_id: Source node ID
            to_id: Target node ID
            link_type: Link type (e.g., 'uses', 'governed_by')
        
        Returns:
            UpdateResult
        """
        if not self.loaded:
            return UpdateResult(False, "File not loaded")
        
        # Find node index
        node_index = self.updater._find_node_index(from_id)
        if node_index is None:
            return UpdateResult(False, f"Node '{from_id}' not found")
        
        # Determine array name
        graph_type = self.updater.data.get('graphType')
        if graph_type == 'skills':
            array_name = 'skills'
        elif graph_type == 'behaviors':
            array_name = 'behaviors'
        elif graph_type in ['knowledge', 'project-graph']:
            array_name = 'nodes'
        else:
            return UpdateResult(False, f"Unknown graphType '{graph_type}'")
        
        # Get current links
        node = self.updater.data[array_name][node_index]
        links = node.get('links', {})
        link_array = links.get(link_type, [])
        
        # Add link if not present
        if to_id in link_array:
            return UpdateResult(True, f"Link already exists: {from_id} --{link_type}--> {to_id}")
        
        link_array.append(to_id)
        links[link_type] = link_array
        
        # Create patch to update links
        patch = [
            {"op": "replace", "path": f"/{array_name}/{node_index}/links", "value": links}
        ]
        
        return self.updater.apply_patch(patch)


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='High-level KG editor')
    parser.add_argument('file', help='Path to JSON KG file')
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Validate command
    subparsers.add_parser('validate', help='Validate KG file')
    
    # Add skill command
    add_skill = subparsers.add_parser('add-skill', help='Add a skill node')
    add_skill.add_argument('--id', required=True, help='Skill ID')
    add_skill.add_argument('--name', required=True, help='Skill name')
    add_skill.add_argument('--category', required=True, help='Skill category')
    add_skill.add_argument('--description', default='', help='Description')
    add_skill.add_argument('--path', default='', help='Path to markdown file')
    add_skill.add_argument('--parent', default='skill:manager:root', help='Parent skill ID')
    
    # Add link command
    add_link = subparsers.add_parser('add-link', help='Add a link between nodes')
    add_link.add_argument('--from', dest='from_id', required=True, help='Source node ID')
    add_link.add_argument('--to', dest='to_id', required=True, help='Target node ID')
    add_link.add_argument('--type', dest='link_type', required=True, help='Link type')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        exit(1)
    
    # Create editor
    editor = KGEditor(args.file)
    
    if not editor.load():
        exit(1)
    
    # Execute command
    if args.command == 'validate':
        result = editor.validate()
        print(result)
        exit(0 if result.is_valid else 1)
    
    elif args.command == 'add-skill':
        result = editor.add_skill(
            id=args.id,
            name=args.name,
            category=args.category,
            description=args.description,
            path=args.path,
            parent=args.parent
        )
        print(result)
        
        if result.success:
            save_result = editor.save()
            print(save_result)
            exit(0 if save_result.success else 1)
        else:
            exit(1)
    
    elif args.command == 'add-link':
        result = editor.add_link(args.from_id, args.to_id, args.link_type)
        print(result)
        
        if result.success:
            save_result = editor.save()
            print(save_result)
            exit(0 if save_result.success else 1)
        else:
            exit(1)


if __name__ == '__main__':
    main()
