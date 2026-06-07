#!/usr/bin/env python3
"""
Fix broken KG links based on LLM analysis
"""

import json
from pathlib import Path

def fix_builder_behaviors():
    """Fix builder-behaviors-graph.json"""
    path = Path("agents/knowledge-graphs/builder-behaviors-graph.json")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Fix: skill:builder:maintain-kg → skill-maintain-kg
    for behavior in data['behaviors']:
        if behavior['id'] == 'behavior:builder:consistency':
            if 'links' in behavior and 'enforces' in behavior['links']:
                behavior['links']['enforces'] = ['skill-maintain-kg']
                print("✓ Fixed: behavior:builder:consistency enforces link")
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved {path}")

def fix_manager_skills():
    """Fix manager-skills-graph.json"""
    path = Path("agents/knowledge-graphs/manager-skills-graph.json")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Fix skill-assess-learning-extractability: remove non-existent links
    for skill in data['skills']:
        if skill['id'] == 'skill-assess-learning-extractability':
            if 'links' in skill:
                # Remove enables and prerequisite_for
                skill['links'].pop('enables', None)
                skill['links'].pop('prerequisite_for', None)
                print("✓ Fixed: skill-assess-learning-extractability removed broken links")
        
        # Fix skill-update-registry: change project-graph → proj:registry
        if skill['id'] == 'skill-update-registry':
            if 'links' in skill and 'operates_on' in skill['links']:
                skill['links']['operates_on'] = ['proj:registry']
                print("✓ Fixed: skill-update-registry operates_on link")
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Saved {path}")

def main():
    print("🔧 Fixing broken KG links...")
    print()
    
    fix_builder_behaviors()
    print()
    fix_manager_skills()
    print()
    print("✅ All fixes applied!")

if __name__ == '__main__':
    main()
