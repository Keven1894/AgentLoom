#!/usr/bin/env python3
"""
JSON Knowledge Graph Node Generator

Template-based generation of KG nodes with auto-completion of required fields.
"""

import json
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime


class NodeGenerator:
    """Generate KG nodes from templates"""
    
    def __init__(self):
        """Initialize generator"""
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load node templates"""
        return {
            'skill': {
                'id': '',
                'name': '',
                'category': '',
                'description': '',
                'path': '',
                'parent': 'skill:manager:root',
                'created': datetime.now().strftime('%Y-%m-%d'),
                'links': {}
            },
            'project': {
                'id': '',
                'type': 'project',
                'category': '',
                'path': '',
                'title': '',
                'status': 'active',
                'description': ''
            },
            'document': {
                'id': '',
                'type': 'document',
                'path': '',
                'title': '',
                'parent': ''
            }
        }
    
    def create_skill(self, id: str, name: str, category: str, 
                    description: str = '', path: str = '', 
                    parent: str = 'skill:manager:root',
                    **kwargs) -> Dict:
        """
        Create a skill node
        
        Args:
            id: Skill ID (e.g., 'skill-new-skill')
            name: Human-readable name
            category: Skill category
            description: Detailed description
            path: Path to skill markdown file
            parent: Parent skill ID
            **kwargs: Additional fields (links, etc.)
        
        Returns:
            Skill node dict
        """
        skill = self.templates['skill'].copy()
        skill.update({
            'id': id,
            'name': name,
            'category': category,
            'description': description,
            'path': path or f'agents/skills/manager/{id}.md',
            'parent': parent,
            'created': datetime.now().strftime('%Y-%m-%d')
        })
        
        # Add any additional fields
        for key, value in kwargs.items():
            skill[key] = value
        
        return skill
    
    def create_project(self, id: str, category: str, path: str,
                      title: str, description: str = '',
                      status: str = 'active') -> Dict:
        """
        Create a project node
        
        Args:
            id: Project ID with category prefix (e.g., 'work:project-name')
            category: Category (work/personal/public/private)
            path: Relative path to project
            title: Project title
            description: Project description
            status: Project status (active/archived/planned)
        
        Returns:
            Project node dict
        """
        project = self.templates['project'].copy()
        project.update({
            'id': id,
            'category': category,
            'path': path,
            'title': title,
            'description': description,
            'status': status
        })
        
        return project
    
    def create_document(self, id: str, path: str, title: str,
                       parent: str) -> Dict:
        """
        Create a document node
        
        Args:
            id: Document ID (e.g., 'doc:project:identity')
            path: Path to document file
            title: Document title
            parent: Parent project ID
        
        Returns:
            Document node dict
        """
        document = self.templates['document'].copy()
        document.update({
            'id': id,
            'path': path,
            'title': title,
            'parent': parent
        })
        
        return document
    
    def generate_template(self, node_type: str, output_file: Optional[Path] = None) -> Dict:
        """
        Generate a template for a node type
        
        Args:
            node_type: Type of node (skill/project/document)
            output_file: Optional file to save template to
        
        Returns:
            Template dict
        """
        if node_type not in self.templates:
            raise ValueError(f"Unknown node type: {node_type}. Available: {list(self.templates.keys())}")
        
        template = self.templates[node_type].copy()
        
        if output_file:
            output_file = Path(output_file)
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2, ensure_ascii=False)
            print(f"✓ Template saved to {output_file}")
        
        return template


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate KG node templates')
    parser.add_argument('type', choices=['skill', 'project', 'document'],
                       help='Type of node to generate')
    parser.add_argument('--output', '-o', help='Output file path')
    
    args = parser.parse_args()
    
    generator = NodeGenerator()
    template = generator.generate_template(args.type, args.output)
    
    if not args.output:
        print(json.dumps(template, indent=2))


if __name__ == '__main__':
    main()
