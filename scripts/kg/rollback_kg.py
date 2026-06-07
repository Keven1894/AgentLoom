#!/usr/bin/env python3
"""
KG Rollback Tool - Quality Control
===================================

Restore Knowledge Graph from backup when issues detected.

Usage:
    python rollback_kg.py --role builder --list
    python rollback_kg.py --role builder --backup backup_20251229_201530
    python rollback_kg.py --role domain --latest
"""

import json
import argparse
import shutil
from pathlib import Path
from datetime import datetime

WORKSPACE = Path(__file__).parent.parent.parent
KG_DIR = WORKSPACE / 'agents' / 'knowledge-graphs'
DASHBOARD_DIR = WORKSPACE / 'dashboards' / 'data'

def list_backups(role: str):
    """List available backups"""
    if role == 'builder':
        pattern = "builder-knowledge-graph.backup_*"
    else:
        pattern = "domain-docs-graph.backup_*"
    backups = sorted(KG_DIR.glob(pattern), reverse=True)
    
    print(f"\n{'='*60}")
    print(f"Available Backups for {role.upper()} KG")
    print('='*60)
    
    if not backups:
        print("No backups found")
        return
    
    for i, backup in enumerate(backups[:20], 1):
        # Extract timestamp from filename
        timestamp_str = backup.stem.split('_')[-2:]  # YYYYMMDD_HHMMSS
        try:
            timestamp = datetime.strptime('_'.join(timestamp_str), '%Y%m%d_%H%M%S')
            age = datetime.now() - timestamp
            days = age.days
            hours = age.seconds // 3600
            
            size_mb = backup.stat().st_size / (1024 * 1024)
            
            print(f"\n{i}. {backup.name}")
            print(f"   Created: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Age: {days}d {hours}h ago")
            print(f"   Size: {size_mb:.2f} MB")
        except Exception as e:
            print(f"\n{i}. {backup.name}")
            print(f"   (Unable to parse timestamp: {e})")
    
    print(f"\n{'='*60}")

def restore_backup(role: str, backup_name: str = None, latest: bool = False, dry_run: bool = False):
    """Restore KG from backup"""
    # Find backup file
    if latest:
        if role == 'builder':
            pattern = "builder-knowledge-graph.backup_*"
        else:
            pattern = "domain-docs-graph.backup_*"
        backups = sorted(KG_DIR.glob(pattern), reverse=True)
        if not backups:
            print(f"[ERROR] No backups found for {role}")
            return False
        backup_file = backups[0]
    elif backup_name:
        # Try with full filename
        backup_file = KG_DIR / backup_name
        if not backup_file.exists():
            # Try constructing filename
            if role == 'builder':
                backup_file = KG_DIR / f"builder-knowledge-graph.json.{backup_name}"
            else:
                backup_file = KG_DIR / f"domain-docs-graph.json.{backup_name}"
        if not backup_file.exists():
            print(f"[ERROR] Backup not found: {backup_name}")
            return False
    else:
        print("[ERROR] Must specify --backup or --latest")
        return False
    
    # Target files
    kg_file = KG_DIR / f"{role}-knowledge-graph.json" if role == 'builder' else KG_DIR / f"{role}-docs-graph.json"
    dashboard_file = DASHBOARD_DIR / kg_file.name
    
    print(f"\n{'='*60}")
    print(f"Rollback Plan for {role.upper()} KG")
    print('='*60)
    print(f"\nBackup: {backup_file.name}")
    print(f"Target KG: {kg_file.name}")
    print(f"Dashboard: {dashboard_file.name}")
    
    if dry_run:
        print("\n[DRY-RUN] Would restore files")
        print('='*60)
        return True
    
    # Confirm
    response = input("\nProceed with rollback? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("[CANCELLED] Rollback aborted")
        return False
    
    # Create safety backup of current state
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safety_backup = kg_file.with_suffix(f'.json.before_rollback_{timestamp}')
    
    try:
        print(f"\n[BACKUP] Creating safety backup...")
        shutil.copy2(kg_file, safety_backup)
        print(f"  Saved: {safety_backup.name}")
        
        print(f"\n[RESTORE] Restoring from backup...")
        shutil.copy2(backup_file, kg_file)
        print(f"  Restored: {kg_file.name}")
        
        print(f"\n[SYNC] Syncing to dashboard...")
        shutil.copy2(kg_file, dashboard_file)
        print(f"  Synced: {dashboard_file.name}")
        
        print(f"\n{'='*60}")
        print("[SUCCESS] Rollback completed!")
        print('='*60)
        print(f"\nSafety backup: {safety_backup.name}")
        print(f"To undo this rollback, use: --backup {safety_backup.name}")
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Rollback failed: {e}")
        print(f"[INFO] Attempting to restore from safety backup...")
        try:
            shutil.copy2(safety_backup, kg_file)
            print("[SUCCESS] Restored from safety backup")
        except:
            print("[CRITICAL] Could not restore from safety backup!")
        return False

def main():
    parser = argparse.ArgumentParser(description="Rollback KG from backup")
    parser.add_argument('--role', required=True, choices=['builder', 'domain'], help="KG role")
    parser.add_argument('--list', action='store_true', help="List available backups")
    parser.add_argument('--backup', help="Specific backup name or timestamp")
    parser.add_argument('--latest', action='store_true', help="Use latest backup")
    parser.add_argument('--dry-run', action='store_true', help="Dry run (no changes)")
    
    args = parser.parse_args()
    
    if args.list:
        list_backups(args.role)
        return 0
    
    success = restore_backup(args.role, args.backup, args.latest, args.dry_run)
    return 0 if success else 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
