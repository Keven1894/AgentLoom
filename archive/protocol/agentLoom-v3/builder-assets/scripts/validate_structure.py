import os
import sys
from pathlib import Path

def check_structure():
    """Validates project folder structure"""
    print("🔍 Validating project structure...\n")
    
    required_dirs = [
        '.cursor',
        'agents',
        'agents/behaviors',
        'agents/behaviors/core',
        'agents/behaviors/builder',
        'agents/behaviors/manager',
        'agents/knowledge-graphs',
        'agents/skills',
        'agents/skills/system',
        'agents/skills/orchestration',
        'docs',
        'scripts',
        'public',
        'personal',
        'work'
    ]
    
    required_files = [
        '.cursor/identity.md',
        '.cursor/project-registry.json',
        'agents/NEW_AGENT_START_HERE.md',
        'agents/USER_MANUAL.md',
        'agents/knowledge-graphs/master-graph.json',
        'docs/CONTENT_TEMPLATE.md'
    ]
    
    print("Directories:")
    dirs_ok = 0
    for dir_path in required_dirs:
        exists = os.path.isdir(dir_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {dir_path}")
        if exists:
            dirs_ok += 1
    
    print(f"\n{dirs_ok}/{len(required_dirs)} required directories present\n")
    
    print("Core Files:")
    files_ok = 0
    for file_path in required_files:
        exists = os.path.isfile(file_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if exists:
            files_ok += 1
    
    print(f"\n{files_ok}/{len(required_files)} required files present\n")
    
    all_ok = (dirs_ok == len(required_dirs)) and (files_ok == len(required_files))
    
    if all_ok:
        print("✅ Project structure is valid!")
        return True
    else:
        print("⚠️  Project structure is incomplete")
        return False

if __name__ == '__main__':
    success = check_structure()
    sys.exit(0 if success else 1)

