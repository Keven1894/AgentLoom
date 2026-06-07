#!/usr/bin/env python3
"""
KG Monitor - Detects file system changes
Monitors directories for new/deleted files and compares with KG

This script is 95% reusable.
Customize: Update MONITORED_DIRS list (line 25) for your project.
"""

import json
from pathlib import Path
from datetime import datetime


# ============================================================================
# CONFIGURATION - Customize this section for your project
# ============================================================================

MONITORED_DIRS = [
    '.cursor/behaviors',
    'agents/skills',
    'docs'
]

# ============================================================================
# No changes needed below this line
# ============================================================================


def extract_paths_from_graphs(kg_dir='agents/knowledge-graphs'):
    """Extract all file paths from KG JSON files"""
    kg_paths = set()
    
    kg_path = Path(kg_dir)
    if not kg_path.exists():
        return kg_paths
    
    for json_file in kg_path.glob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                nodes = data.get('nodes', []) or data.get('skills', []) or data.get('behaviors', [])
                for node in nodes:
                    if 'path' in node:
                        kg_paths.add(node['path'])
        except Exception as e:
            print(f"Warning: Could not read {json_file}: {e}")
    
    return kg_paths


def scan_directories(directories):
    """Scan directories for markdown files"""
    actual_paths = set()
    
    for directory in directories:
        dir_path = Path(directory)
        if dir_path.exists():
            for md_file in dir_path.rglob('*.md'):
                actual_paths.add(str(md_file))
    
    return actual_paths


def monitor_changes():
    """Main monitoring function"""
    kg_paths = extract_paths_from_graphs()
    actual_paths = scan_directories(MONITORED_DIRS)
    
    added = actual_paths - kg_paths
    deleted = kg_paths - actual_paths
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "added": sorted(list(added)),
        "deleted": sorted(list(deleted)),
        "monitored_files": len(actual_paths),
        "kg_files": len(kg_paths)
    }
    
    return report


if __name__ == '__main__':
    report = monitor_changes()
    
    print(f"KG Monitor Report - {report['timestamp']}")
    print("=" * 60)
    print(f"Files in monitored directories: {report['monitored_files']}")
    print(f"Files in Knowledge Graph: {report['kg_files']}")
    
    if report['added']:
        print(f"\n✨ New files detected ({len(report['added'])}):")
        for path in report['added']:
            print(f"  + {path}")
    
    if report['deleted']:
        print(f"\n🗑️  Deleted files detected ({len(report['deleted'])}):")
        for path in report['deleted']:
            print(f"  - {path}")
    
    if not report['added'] and not report['deleted']:
        print("\n✅ No changes detected")
    
    # Output JSON for programmatic use
    print("\n" + "=" * 60)
    print("JSON Output:")
    print(json.dumps(report, indent=2))
