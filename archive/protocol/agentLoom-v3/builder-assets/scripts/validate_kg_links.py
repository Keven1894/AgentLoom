#!/usr/bin/env python3
"""
Knowledge Graph Link Validator

Validates cross-references and connectivity across all knowledge graphs.
Can auto-fix broken links and orphaned nodes.

Usage:
    python scripts/validate_kg_links.py              # Report only
    python scripts/validate_kg_links.py --fix        # Auto-fix issues
    python scripts/validate_kg_links.py --verbose    # Detailed output
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class KGValidator:
    def __init__(self, project_root: Path, verbose: bool = False):
        self.project_root = project_root
        self.verbose = verbose
        self.graphs = {}
        self.node_index = {}
        self.issues = []
        self.warnings = []
        
    def load_all_graphs(self) -> bool:
        """Load all knowledge graph JSON files"""
        graph_files = [
            "agents/knowledge-graphs/master-graph.json",
            "agents/knowledge-graphs/builder-skills-graph.json",
            "agents/knowledge-graphs/builder-behaviors-graph.json",
            "agents/knowledge-graphs/builder-knowledge-graph.json",
            "agents/knowledge-graphs/manager-skills-graph.json",
            "agents/knowledge-graphs/manager-behaviors-graph.json",
            "agents/knowledge-graphs/manager-knowledge-graph.json",
        ]
        
        for graph_file in graph_files:
            path = self.project_root / graph_file
            if not path.exists():
                self.issues.append(f"Missing graph file: {graph_file}")
                continue
                
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    self.graphs[graph_file] = json.load(f)
                if self.verbose:
                    print(f"✓ Loaded {graph_file}")
            except json.JSONDecodeError as e:
                self.issues.append(f"Invalid JSON in {graph_file}: {e}")
                return False
                
        return len(self.issues) == 0
    
    def build_node_index(self):
        """Build index of all nodes by ID"""
        for graph_file, graph_data in self.graphs.items():
            if graph_file == "agents/knowledge-graphs/master-graph.json":
                continue
                
            # Index skills
            if 'skills' in graph_data:
                for skill in graph_data['skills']:
                    node_id = skill.get('id')
                    if node_id:
                        self.node_index[node_id] = {
                            'type': 'skill',
                            'graph': graph_file,
                            'data': skill
                        }
            
            # Index behaviors
            if 'behaviors' in graph_data:
                for behavior in graph_data['behaviors']:
                    node_id = behavior.get('id')
                    if node_id:
                        self.node_index[node_id] = {
                            'type': 'behavior',
                            'graph': graph_file,
                            'data': behavior
                        }
            
            # Index knowledge nodes
            if 'nodes' in graph_data:
                for node in graph_data['nodes']:
                    node_id = node.get('id')
                    if node_id:
                        self.node_index[node_id] = {
                            'type': 'knowledge',
                            'graph': graph_file,
                            'data': node
                        }
        
        if self.verbose:
            print(f"✓ Indexed {len(self.node_index)} nodes")
    
    def validate_cross_references(self) -> List[Dict]:
        """Validate all link references"""
        broken_links = []
        
        link_types_to_validate = [
            'governed_by', 'guides', 'depends_on', 'enforces', 
            'implements', 'extends', 'synergizes_with', 'applies_to',
            'references', 'enables', 'prerequisite_for', 'superseded_by',
            'operates_on', 'constrains', 'protects', 'validates'
        ]
        
        for node_id, node_info in self.node_index.items():
            node_data = node_info['data']
            links = node_data.get('links', {})
            
            for link_type in link_types_to_validate:
                if link_type not in links:
                    continue
                    
                targets = links[link_type]
                if not isinstance(targets, list):
                    targets = [targets]
                
                for target in targets:
                    # Skip file paths and categories
                    if '/' in target or '.' in target or target.startswith('cat:') or target.startswith('sys:') or target.startswith('proj:') or target.startswith('docs:'):
                        continue
                    
                    if target not in self.node_index:
                        broken_links.append({
                            'source': node_id,
                            'source_graph': node_info['graph'],
                            'link_type': link_type,
                            'target': target,
                            'severity': 'ERROR'
                        })
        
        return broken_links
    
    def validate_connectivity(self) -> List[Dict]:
        """Check node connectivity"""
        orphaned = []
        
        for node_id, node_info in self.node_index.items():
            node_data = node_info['data']
            
            # Skip root nodes
            if node_data.get('type') == 'root':
                continue
            
            links = node_data.get('links', {})
            
            # Skills must have governed_by
            if node_info['type'] == 'skill' and 'governed_by' not in links:
                orphaned.append({
                    'id': node_id,
                    'graph': node_info['graph'],
                    'issue': 'Missing governed_by link',
                    'severity': 'WARNING'
                })
            
            # Warn if node has no links at all
            if not links or len(links) == 0:
                orphaned.append({
                    'id': node_id,
                    'graph': node_info['graph'],
                    'issue': 'No links (orphaned node)',
                    'severity': 'WARNING'
                })
        
        return orphaned
    
    def validate_file_existence(self) -> List[Dict]:
        """Check if files referenced in 'path' field actually exist"""
        missing_files = []
        
        for node_id, node_info in self.node_index.items():
            node_data = node_info['data']
            path = node_data.get('path')
            
            if not path:
                continue
            
            # Construct full path
            full_path = self.project_root / path
            
            if not full_path.exists():
                missing_files.append({
                    'id': node_id,
                    'graph': node_info['graph'],
                    'path': path,
                    'issue': f'Referenced file does not exist: {path}',
                    'severity': 'ERROR'
                })
        
        return missing_files

    
    def validate_master_graph(self) -> List[Dict]:
        """Validate master-graph.json"""
        issues = []
        master = self.graphs.get("agents/knowledge-graphs/master-graph.json", {})
        
        if not master:
            issues.append({
                'issue': 'master-graph.json not found',
                'severity': 'ERROR'
            })
            return issues
        
        # Check all listed graphs exist
        for graph_entry in master.get('graphs', []):
            graph_path = graph_entry.get('path')
            if graph_path and graph_path not in self.graphs:
                issues.append({
                    'issue': f"Graph listed in master but not found: {graph_path}",
                    'severity': 'ERROR'
                })
        
        # Check roles reference valid graphs
        for role in master.get('roles', []):
            role_graphs = role.get('graphs', [])
            for graph_id in role_graphs:
                # Find if this graph_id exists in graphs list
                found = any(g.get('id') == graph_id for g in master.get('graphs', []))
                if not found:
                    issues.append({
                        'issue': f"Role '{role.get('name')}' references unknown graph: {graph_id}",
                        'severity': 'ERROR'
                    })
        
        return issues
    
    def auto_fix(self, broken_links: List[Dict], orphaned: List[Dict]) -> int:
        """Auto-fix issues (remove broken links, warn about orphans)"""
        fixes_made = 0
        
        # Group broken links by source graph
        links_by_graph = {}
        for link in broken_links:
            graph = link['source_graph']
            if graph not in links_by_graph:
                links_by_graph[graph] = []
            links_by_graph[graph].append(link)
        
        # Fix each graph
        for graph_file, links_to_fix in links_by_graph.items():
            graph_data = self.graphs[graph_file]
            modified = False
            
            for link_issue in links_to_fix:
                source_id = link_issue['source']
                link_type = link_issue['link_type']
                target = link_issue['target']
                
                # Find and fix the node
                nodes_list = graph_data.get('skills') or graph_data.get('behaviors') or graph_data.get('nodes', [])
                for node in nodes_list:
                    if node.get('id') == source_id:
                        if 'links' in node and link_type in node['links']:
                            targets = node['links'][link_type]
                            if isinstance(targets, list):
                                if target in targets:
                                    targets.remove(target)
                                    modified = True
                                    fixes_made += 1
                                    print(f"  ✓ Removed broken link: {source_id} -[{link_type}]-> {target}")
                                    
                                    # Remove empty link type
                                    if len(targets) == 0:
                                        del node['links'][link_type]
                            elif targets == target:
                                del node['links'][link_type]
                                modified = True
                                fixes_made += 1
                                print(f"  ✓ Removed broken link: {source_id} -[{link_type}]-> {target}")
            
            # Save modified graph
            if modified:
                path = self.project_root / graph_file
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(graph_data, f, indent=2)
                print(f"✓ Saved fixes to {graph_file}")
        
        return fixes_made
    
    def generate_report(self, broken_links: List[Dict], orphaned: List[Dict], missing_files: List[Dict], master_issues: List[Dict]) -> Dict:
        """Generate validation report"""
        total_nodes = len(self.node_index)
        total_links = sum(
            len(node['data'].get('links', {}))
            for node in self.node_index.values()
        )
        
        status = "PASS" if (len(broken_links) == 0 and len(missing_files) == 0 and len(master_issues) == 0) else "FAIL"
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_nodes": total_nodes,
                "total_links": total_links,
                "broken_links": len(broken_links),
                "missing_files": len(missing_files),
                "orphaned_nodes": len(orphaned),
                "master_issues": len(master_issues),
                "status": status
            },
            "broken_links": broken_links,
            "missing_files": missing_files,
            "orphaned_nodes": orphaned,
            "master_issues": master_issues,
            "suggestions": []
        }
        
        # Generate suggestions
        if missing_files:
            report["suggestions"].append(f"Fix {len(missing_files)} missing file references")
        if orphaned:
            report["suggestions"].append(f"Review {len(orphaned)} orphaned/disconnected nodes")
        if broken_links:
            report["suggestions"].append(f"Fix {len(broken_links)} broken cross-references")
        if master_issues:
            report["suggestions"].append(f"Fix {len(master_issues)} master graph issues")
        
        return report
    
    def run(self, auto_fix: bool = False) -> Tuple[bool, Dict]:
        """Run validation"""
        print("🔍 Validating Knowledge Graphs...")
        print()
        
        # Load graphs
        if not self.load_all_graphs():
            return False, {"error": "Failed to load graphs", "issues": self.issues}
        
        # Build index
        self.build_node_index()
        
        # Validate
        print("Validating cross-references...")
        broken_links = self.validate_cross_references()
        
        print("Validating file existence...")
        missing_files = self.validate_file_existence()
        
        print("Validating connectivity...")
        orphaned = self.validate_connectivity()
        
        print("Validating master graph...")
        master_issues = self.validate_master_graph()
        
        # Auto-fix if requested
        if auto_fix and broken_links:
            print()
            print("🔧 Auto-fixing broken links...")
            fixes_made = self.auto_fix(broken_links, orphaned)
            print(f"✓ Fixed {fixes_made} broken links")
            
            # Re-validate after fixes
            self.load_all_graphs()
            self.build_node_index()
            broken_links = self.validate_cross_references()
            missing_files = self.validate_file_existence()
        
        # Generate report
        report = self.generate_report(broken_links, orphaned, missing_files, master_issues)
        
        # Print summary
        print()
        print("=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Total Nodes: {report['summary']['total_nodes']}")
        print(f"Total Links: {report['summary']['total_links']}")
        print(f"Broken Links: {report['summary']['broken_links']}")
        print(f"Missing Files: {report['summary']['missing_files']}")
        print(f"Orphaned Nodes: {report['summary']['orphaned_nodes']}")
        print(f"Master Issues: {report['summary']['master_issues']}")
        print(f"Status: {report['summary']['status']}")
        print("=" * 60)
        
        if broken_links:
            print()
            print("❌ BROKEN LINKS:")
            for link in broken_links[:10]:  # Show first 10
                print(f"  {link['source']} -[{link['link_type']}]-> {link['target']}")
            if len(broken_links) > 10:
                print(f"  ... and {len(broken_links) - 10} more")
        
        missing_files = report.get('missing_files', [])
        if missing_files:
            print()
            print("❌ MISSING FILES:")
            for file in missing_files[:10]:  # Show first 10
                print(f"  {file['id']}: {file['path']}")
            if len(missing_files) > 10:
                print(f"  ... and {len(missing_files) - 10} more")
        
        if orphaned:
            print()
            print("⚠️  ORPHANED/DISCONNECTED NODES:")
            for node in orphaned[:10]:  # Show first 10
                print(f"  {node['id']}: {node['issue']}")
            if len(orphaned) > 10:
                print(f"  ... and {len(orphaned) - 10} more")
        
        if master_issues:
            print()
            print("❌ MASTER GRAPH ISSUES:")
            for issue in master_issues:
                print(f"  {issue['issue']}")
        
        success = report['summary']['status'] == 'PASS'
        return success, report


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Knowledge Graph Links')
    parser.add_argument('--fix', action='store_true', help='Auto-fix broken links')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--output', type=str, help='Save report to JSON file')
    
    args = parser.parse_args()
    
    # Find project root
    project_root = Path(__file__).parent.parent
    
    # Run validation
    validator = KGValidator(project_root, verbose=args.verbose)
    success, report = validator.run(auto_fix=args.fix)
    
    # Save report if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n✓ Report saved to {args.output}")
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
