#!/usr/bin/env python3
"""
JSON Knowledge Graph Validator

Validates JSON KG files against their schemas using jsonschema.
Provides detailed error reporting and validation results.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import jsonschema
from jsonschema import Draft7Validator, validators


@dataclass
class ValidationResult:
    """Result of a validation operation"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    file_path: Optional[Path] = None
    
    def __str__(self) -> str:
        if self.is_valid:
            status = "✅ VALID"
        else:
            status = f"❌ INVALID ({len(self.errors)} errors)"
        
        result = [f"{status}: {self.file_path or 'JSON data'}"]
        
        if self.errors:
            result.append("\nErrors:")
            for i, error in enumerate(self.errors, 1):
                result.append(f"  {i}. {error}")
        
        if self.warnings:
            result.append("\nWarnings:")
            for i, warning in enumerate(self.warnings, 1):
                result.append(f"  {i}. {warning}")
        
        return "\n".join(result)


class KGValidator:
    """JSON Knowledge Graph Validator"""
    
    def __init__(self, schemas_dir: Optional[Path] = None):
        """
        Initialize validator
        
        Args:
            schemas_dir: Directory containing JSON schema files
                        Defaults to scripts/json-helper/schemas/
        """
        if schemas_dir is None:
            # Default to schemas/ directory next to this file
            schemas_dir = Path(__file__).parent / "schemas"
        
        self.schemas_dir = Path(schemas_dir)
        self.schemas: Dict[str, dict] = {}
        self._load_schemas()
    
    def _load_schemas(self):
        """Load all JSON schemas from schemas directory"""
        if not self.schemas_dir.exists():
            raise FileNotFoundError(f"Schemas directory not found: {self.schemas_dir}")
        
        for schema_file in self.schemas_dir.glob("*.schema.json"):
            try:
                with open(schema_file, 'r', encoding='utf-8') as f:
                    schema = json.load(f)
                
                # Extract schema name from filename
                # e.g., "skills-graph.schema.json" -> "skills-graph"
                schema_name = schema_file.stem.replace('.schema', '')
                self.schemas[schema_name] = schema
                
            except Exception as e:
                print(f"⚠️  Failed to load schema {schema_file}: {e}")
    
    def get_schema_for_graph_type(self, graph_type: str) -> Optional[dict]:
        """
        Get schema for a specific graph type
        
        Args:
            graph_type: Graph type (e.g., 'skills', 'project-graph')
        
        Returns:
            Schema dict or None if not found
        """
        # Map graph types to schema names
        schema_map = {
            'skills': 'skills-graph',
            'behaviors': 'behaviors-graph',
            'knowledge': 'knowledge-graph',
            'project-graph': 'project-graph'
        }
        
        schema_name = schema_map.get(graph_type)
        if schema_name:
            return self.schemas.get(schema_name)
        
        return None
    
    def validate_data(self, data: dict, schema: Optional[dict] = None) -> ValidationResult:
        """
        Validate JSON data against a schema
        
        Args:
            data: JSON data to validate
            schema: Schema to validate against. If None, auto-detect from graphType
        
        Returns:
            ValidationResult with errors and warnings
        """
        errors = []
        warnings = []
        
        # Auto-detect schema if not provided
        if schema is None:
            graph_type = data.get('graphType')
            if not graph_type:
                errors.append("Missing 'graphType' field - cannot auto-detect schema")
                return ValidationResult(False, errors, warnings)
            
            schema = self.get_schema_for_graph_type(graph_type)
            if not schema:
                errors.append(f"No schema found for graphType '{graph_type}'")
                return ValidationResult(False, errors, warnings)
        
        # Validate against schema
        try:
            validator = Draft7Validator(schema)
            validation_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            
            for error in validation_errors:
                # Format error message
                path = ".".join(str(p) for p in error.path) if error.path else "root"
                message = f"At '{path}': {error.message}"
                errors.append(message)
            
        except jsonschema.SchemaError as e:
            errors.append(f"Invalid schema: {e.message}")
        except Exception as e:
            errors.append(f"Validation error: {str(e)}")
        
        # Additional custom validations (warnings)
        warnings.extend(self._custom_validations(data))
        
        is_valid = len(errors) == 0
        return ValidationResult(is_valid, errors, warnings)
    
    def validate_file(self, file_path: Path) -> ValidationResult:
        """
        Validate a JSON file
        
        Args:
            file_path: Path to JSON file
        
        Returns:
            ValidationResult
        """
        file_path = Path(file_path)
        errors = []
        warnings = []
        
        # Check file exists
        if not file_path.exists():
            errors.append(f"File not found: {file_path}")
            return ValidationResult(False, errors, warnings, file_path)
        
        # Load JSON
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON: {e.msg} at line {e.lineno}, column {e.colno}")
            return ValidationResult(False, errors, warnings, file_path)
        except Exception as e:
            errors.append(f"Failed to read file: {str(e)}")
            return ValidationResult(False, errors, warnings, file_path)
        
        # Validate data
        result = self.validate_data(data)
        result.file_path = file_path
        return result
    
    def _custom_validations(self, data: dict) -> List[str]:
        """
        Custom validation rules beyond schema
        
        Args:
            data: JSON data
        
        Returns:
            List of warning messages
        """
        warnings = []
        graph_type = data.get('graphType')
        
        # Skills graph validations
        if graph_type == 'skills':
            skills = data.get('skills', [])
            
            # Check for duplicate IDs
            ids = [s.get('id') for s in skills if s.get('id')]
            duplicates = [id for id in ids if ids.count(id) > 1]
            if duplicates:
                warnings.append(f"Duplicate skill IDs found: {set(duplicates)}")
            
            # Check for orphaned skills (no parent except root)
            root_ids = [s.get('id') for s in skills if s.get('type') == 'root']
            for skill in skills:
                if skill.get('type') != 'root' and not skill.get('parent'):
                    warnings.append(f"Skill '{skill.get('id')}' has no parent")
        
        # Project graph validations
        elif graph_type == 'project-graph':
            nodes = data.get('nodes', [])
            
            # Check for duplicate IDs
            ids = [n.get('id') for n in nodes if n.get('id')]
            duplicates = [id for id in ids if ids.count(id) > 1]
            if duplicates:
                warnings.append(f"Duplicate node IDs found: {set(duplicates)}")
            
            # Check document parents exist
            project_ids = {n.get('id') for n in nodes if n.get('type') == 'project'}
            for node in nodes:
                if node.get('type') == 'document':
                    parent = node.get('parent')
                    if parent and parent not in project_ids:
                        warnings.append(f"Document '{node.get('id')}' references non-existent parent '{parent}'")
        
        return warnings


def main():
    """CLI entry point for validator"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate JSON Knowledge Graph files')
    parser.add_argument('file', help='Path to JSON file to validate')
    parser.add_argument('--schemas', help='Path to schemas directory')
    
    args = parser.parse_args()
    
    # Create validator
    validator = KGValidator(schemas_dir=args.schemas if args.schemas else None)
    
    # Validate file
    result = validator.validate_file(args.file)
    
    # Print result
    print(result)
    
    # Exit with appropriate code
    exit(0 if result.is_valid else 1)


if __name__ == '__main__':
    main()
