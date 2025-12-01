#!/usr/bin/env python3
"""
Auto-Chunk Document Tool ("The Surgeon")

Splits a large markdown file into smaller chunks based on a provided JSON plan.
This is the "Execution" half of the Hybrid Chunking Skill.

Usage:
    python chunk_document.py <target_file> --plan <plan_json>
    python chunk_document.py <target_file> --dry-run
"""

import os
import sys
import json
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional

def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_markdown_sections(content: str) -> Dict[str, str]:
    """
    Splits markdown into sections by H1/H2 headers.
    Returns a dict: {"Header Name": "Content..."}
    """
    lines = content.split('\n')
    sections = {}
    current_header = "preamble"
    current_content = []
    
    for line in lines:
        # Match H1 or H2 headers
        if line.startswith('# ') or line.startswith('## '):
            # Save previous section
            if current_content:
                sections[current_header] = '\n'.join(current_content)
            
            # Start new section
            current_header = line.strip()
            current_content = [line]
        else:
            current_content.append(line)
            
    # Save last section
    if current_content:
        sections[current_header] = '\n'.join(current_content)
        
    return sections

def execute_split(target_file: str, plan_path: str, dry_run: bool = False):
    print(f"🔪 Starting surgery on: {target_file}")
    
    # 1. Read Target File
    content = read_file(target_file)
    original_lines = len(content.split('\n'))
    print(f"   Original size: {original_lines} lines")
    
    # 2. Read Plan
    try:
        plan = json.loads(read_file(plan_path))
    except Exception as e:
        print(f"❌ Error reading plan: {e}")
        sys.exit(1)
        
    # 3. Parse Content by Sections
    sections_map = parse_markdown_sections(content)
    print(f"   Identified {len(sections_map)} sections")
    
    # 4. Build New Files
    new_files = {}
    
    for chunk in plan['chunks']:
        target_name = chunk['targetName']
        chunk_content = []
        
        # Add frontmatter if specified
        if 'frontmatter' in chunk:
            chunk_content.append(chunk['frontmatter'])
            
        # Add requested sections
        for section_header in chunk['sections']:
            # Fuzzy match header
            found = False
            for key in sections_map:
                if section_header in key: # Simple substring match
                    chunk_content.append(sections_map[key])
                    found = True
                    break
            
            if not found:
                print(f"⚠️ Warning: Section '{section_header}' not found in source file.")
        
        new_files[target_name] = '\n\n'.join(chunk_content)

    # 5. Verify & Write
    total_new_lines = sum(len(c.split('\n')) for c in new_files.values())
    print(f"   Projected new size: {total_new_lines} lines (approx)")
    
    if dry_run:
        print("🔍 Dry Run - No files written.")
        print(json.dumps(list(new_files.keys()), indent=2))
        return

    # Backup original
    backup_path = target_file + ".bak"
    shutil.copy2(target_file, backup_path)
    print(f"   Backup created: {backup_path}")
    
    # Write new files
    base_dir = os.path.dirname(target_file)
    created_paths = []
    
    for name, text in new_files.items():
        full_path = os.path.join(base_dir, name)
        write_file(full_path, text)
        created_paths.append(name)
        print(f"✅ Created: {name} ({len(text.splitlines())} lines)")
        
    # Generate INDEX.md if requested
    if 'index' in plan:
        index_path = os.path.join(base_dir, "INDEX.md")
        write_file(index_path, plan['index']['content'])
        print(f"✅ Created: INDEX.md")

    print("🎉 Surgery complete.")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Target markdown file")
    parser.add_argument("--plan", help="JSON Split Plan file")
    parser.add_argument("--dry-run", action="store_true", help="Simulate only")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print("File not found")
        sys.exit(1)
        
    if args.plan:
        execute_split(args.file, args.plan, args.dry_run)
    else:
        print("Please provide a --plan JSON file.")
        # In future, could invoke LLM here to generate plan
        sys.exit(1)

if __name__ == "__main__":
    main()
