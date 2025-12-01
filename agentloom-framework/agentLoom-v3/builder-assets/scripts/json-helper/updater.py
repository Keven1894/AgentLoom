#!/usr/bin/env python3
"""
JSON Knowledge Graph Updater

Safe atomic updates to JSON KG files using jsonpatch (RFC 6902).
Provides automatic backup, validation, and rollback capabilities.
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Union
from datetime import datetime
from dataclasses import dataclass
import jsonpatch

# Handle both module and standalone script usage
try:
    from .validator import KGValidator, ValidationResult
except ImportError:
    # Running as standalone script
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from validator import KGValidator, ValidationResult


@dataclass
class UpdateResult:
    """Result of an update operation"""
    success: bool
    message: str
    backup_path: Optional[Path] = None
    validation_result: Optional[ValidationResult] = None
    
    def __str__(self) -> str:
        status = "✅ SUCCESS" if self.success else "❌ FAILED"
        result = [f"{status}: {self.message}"]
        
        if self.backup_path:
            result.append(f"Backup: {self.backup_path}")
        
        if self.validation_result and not self.validation_result.is_valid:
            result.append(f"\n{self.validation_result}")
        
        return "\n".join(result)


class KGUpdater:
    """JSON Knowledge Graph Updater using jsonpatch"""
    
    def __init__(self, file_path: Union[str, Path], auto_backup: bool = True, 
                 auto_validate: bool = True):
        """
        Initialize updater
        
        Args:
            file_path: Path to JSON file to update
            auto_backup: Automatically create backup before updates
            auto_validate: Automatically validate before and after updates
        """
        self.file_path = Path(file_path)
        self.auto_backup = auto_backup
        self.auto_validate = auto_validate
        self.validator = KGValidator() if auto_validate else None
        self.data: Optional[dict] = None
        self.original_data: Optional[dict] = None
    
    def load(self) -> bool:
        """
        Load JSON file
        
        Returns:
            True if successful, False otherwise
        """
        if not self.file_path.exists():
            print(f"❌ File not found: {self.file_path}")
            return False
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
                self.original_data = json.loads(json.dumps(self.data))  # Deep copy
            print(f"✓ Loaded {self.file_path}")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return False
        except Exception as e:
            print(f"❌ Load failed: {e}")
            return False
    
    def backup(self) -> Optional[Path]:
        """
        Create timestamped backup of current file
        
        Returns:
            Path to backup file or None if failed
        """
        if not self.file_path.exists():
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.file_path.with_suffix(f'.backup_{timestamp}.json')
        
        try:
            shutil.copy2(self.file_path, backup_path)
            print(f"✓ Backup created: {backup_path}")
            return backup_path
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return None
    
    def validate(self, data: Optional[dict] = None) -> ValidationResult:
        """
        Validate JSON data
        
        Args:
            data: Data to validate (defaults to self.data)
        
        Returns:
            ValidationResult
        """
        if not self.validator:
            # Validation disabled
            return ValidationResult(True, [], [])
        
        data_to_validate = data if data is not None else self.data
        if data_to_validate is None:
            return ValidationResult(False, ["No data loaded"], [])
        
        return self.validator.validate_data(data_to_validate)
    
    def apply_patch(self, patch: List[Dict], in_place: bool = False) -> UpdateResult:
        """
        Apply JSON Patch (RFC 6902) to data
        
        Args:
            patch: List of patch operations
            in_place: If True, modify self.data directly. If False, work on copy.
        
        Returns:
            UpdateResult
        """
        if self.data is None:
            return UpdateResult(False, "No data loaded. Call load() first.")
        
        # Pre-validation
        if self.auto_validate:
            pre_validation = self.validate()
            if not pre_validation.is_valid:
                return UpdateResult(
                    False, 
                    "Pre-validation failed", 
                    validation_result=pre_validation
                )
        
        # Create backup
        backup_path = None
        if self.auto_backup:
            backup_path = self.backup()
            if not backup_path:
                return UpdateResult(False, "Backup failed")
        
        # Apply patch
        try:
            # Work on copy unless in_place=True
            data_to_patch = self.data if in_place else json.loads(json.dumps(self.data))
            
            # Create JsonPatch object
            patch_obj = jsonpatch.JsonPatch(patch)
            
            # Apply patch (atomic operation)
            patched_data = patch_obj.apply(data_to_patch, in_place=in_place)
            
            # Post-validation
            if self.auto_validate:
                post_validation = self.validate(patched_data)
                if not post_validation.is_valid:
                    return UpdateResult(
                        False,
                        "Post-validation failed - patch not applied",
                        backup_path,
                        post_validation
                    )
            
            # Update data
            self.data = patched_data
            
            return UpdateResult(
                True,
                f"Patch applied successfully ({len(patch)} operations)",
                backup_path
            )
            
        except jsonpatch.JsonPatchConflict as e:
            return UpdateResult(
                False,
                f"Patch conflict: {str(e)}",
                backup_path
            )
        except jsonpatch.JsonPatchException as e:
            return UpdateResult(
                False,
                f"Patch error: {str(e)}",
                backup_path
            )
        except Exception as e:
            return UpdateResult(
                False,
                f"Unexpected error: {str(e)}",
                backup_path
            )
    
    def save(self, validate_before_save: bool = True) -> UpdateResult:
        """
        Save data to file
        
        Args:
            validate_before_save: Validate before saving
        
        Returns:
            UpdateResult
        """
        if self.data is None:
            return UpdateResult(False, "No data to save")
        
        # Validate before save
        if validate_before_save and self.auto_validate:
            validation = self.validate()
            if not validation.is_valid:
                return UpdateResult(
                    False,
                    "Validation failed - not saving",
                    validation_result=validation
                )
        
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            
            return UpdateResult(True, f"Saved to {self.file_path}")
            
        except Exception as e:
            return UpdateResult(False, f"Save failed: {str(e)}")
    
    def rollback(self) -> UpdateResult:
        """
        Rollback to original data (before any patches)
        
        Returns:
            UpdateResult
        """
        if self.original_data is None:
            return UpdateResult(False, "No original data to rollback to")
        
        self.data = json.loads(json.dumps(self.original_data))  # Deep copy
        return UpdateResult(True, "Rolled back to original data")
    
    def add_node(self, node: Dict, array_path: str = None) -> UpdateResult:
        """
        Add a node to the graph (high-level helper)
        
        Args:
            node: Node data to add
            array_path: Path to array (e.g., "/skills"). Auto-detected if None.
        
        Returns:
            UpdateResult
        """
        if self.data is None:
            return UpdateResult(False, "No data loaded")
        
        # Auto-detect array path from graph type
        if array_path is None:
            graph_type = self.data.get('graphType')
            if graph_type == 'skills':
                array_path = '/skills'
            elif graph_type == 'behaviors':
                array_path = '/behaviors'
            elif graph_type in ['knowledge', 'project-graph']:
                array_path = '/nodes'
            else:
                return UpdateResult(False, f"Cannot auto-detect array path for graphType '{graph_type}'")
        
        # Create patch to add node at end of array
        patch = [
            {"op": "add", "path": f"{array_path}/-", "value": node}
        ]
        
        return self.apply_patch(patch)
    
    def update_node_field(self, node_id: str, field: str, value: any) -> UpdateResult:
        """
        Update a field in a specific node (high-level helper)
        
        Args:
            node_id: ID of node to update
            field: Field name to update
            value: New value
        
        Returns:
            UpdateResult
        """
        if self.data is None:
            return UpdateResult(False, "No data loaded")
        
        # Find node index
        node_index = self._find_node_index(node_id)
        if node_index is None:
            return UpdateResult(False, f"Node '{node_id}' not found")
        
        # Determine array name
        graph_type = self.data.get('graphType')
        if graph_type == 'skills':
            array_name = 'skills'
        elif graph_type == 'behaviors':
            array_name = 'behaviors'
        elif graph_type in ['knowledge', 'project-graph']:
            array_name = 'nodes'
        else:
            return UpdateResult(False, f"Unknown graphType '{graph_type}'")
        
        # Create patch
        patch = [
            {"op": "replace", "path": f"/{array_name}/{node_index}/{field}", "value": value}
        ]
        
        return self.apply_patch(patch)
    
    def _find_node_index(self, node_id: str) -> Optional[int]:
        """Find index of node with given ID"""
        if self.data is None:
            return None
        
        graph_type = self.data.get('graphType')
        if graph_type == 'skills':
            nodes = self.data.get('skills', [])
        elif graph_type == 'behaviors':
            nodes = self.data.get('behaviors', [])
        elif graph_type in ['knowledge', 'project-graph']:
            nodes = self.data.get('nodes', [])
        else:
            return None
        
        for i, node in enumerate(nodes):
            if node.get('id') == node_id:
                return i
        
        return None


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Update JSON KG files using jsonpatch')
    parser.add_argument('file', help='Path to JSON file')
    parser.add_argument('--patch', help='JSON patch operations (as JSON string)')
    parser.add_argument('--patch-file', help='Path to JSON file containing patch operations')
    parser.add_argument('--no-backup', action='store_true', help='Skip backup creation')
    parser.add_argument('--no-validate', action='store_true', help='Skip validation')
    
    args = parser.parse_args()
    
    # Create updater
    updater = KGUpdater(
        args.file,
        auto_backup=not args.no_backup,
        auto_validate=not args.no_validate
    )
    
    # Load file
    if not updater.load():
        exit(1)
    
    # Get patch operations
    if args.patch:
        try:
            patch = json.loads(args.patch)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid patch JSON: {e}")
            exit(1)
    elif args.patch_file:
        try:
            with open(args.patch_file, 'r') as f:
                patch = json.load(f)
        except Exception as e:
            print(f"❌ Failed to load patch file: {e}")
            exit(1)
    else:
        print("❌ Either --patch or --patch-file required")
        exit(1)
    
    # Apply patch
    result = updater.apply_patch(patch)
    print(result)
    
    if not result.success:
        exit(1)
    
    # Save
    save_result = updater.save()
    print(save_result)
    
    exit(0 if save_result.success else 1)


if __name__ == '__main__':
    main()
