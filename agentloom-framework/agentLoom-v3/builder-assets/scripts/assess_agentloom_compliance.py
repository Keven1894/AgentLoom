"""
AgentLoom V3 Compliance Assessment Script

Purpose: Evaluate 12 agent projects for AgentLoom V3 framework compliance
Output: Detailed compliance report in temp/agentloom_compliance_report_{timestamp}.json

Usage:
    python scripts/assess_agentloom_compliance.py [--project PROJECT_ID]
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import argparse


# Special case projects to exclude from assessment
SPECIAL_CASES = [
    "agentic-ai-research-roadmap-github",
    "agentic-ai-research-roadmap-gitlab",
    "co-agenticOS",
    "agentic-ai-proj-manager"
]


class AgentLoomAssessor:
    """Assesses projects for AgentLoom V3 compliance."""
    
    def __init__(self, projects_root: Path):
        self.projects_root = projects_root
        self.assessments = []
        
    def load_metadata(self) -> Dict[str, Any]:
        """Load projects metadata."""
        metadata_path = self.projects_root / "projects-metadata.json"
        
        if not metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
        
        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def assess_configuration(self, project_path: Path) -> Dict[str, Any]:
        """
        Assess configuration structure (30 points max).
        
        Checks for:
        - .cursor/ folder (15 pts)
        - .cursor/identity.md (5 pts)
        - .cursor/rules.md (5 pts)
        - .cursor/behaviors/ folder (5 pts)
        - Deprecated .cursorrules file (-10 pts)
        """
        score = 0
        max_score = 30
        findings = {
            "score": 0,
            "max": max_score,
            "has_cursor_folder": False,
            "has_identity": False,
            "has_rules": False,
            "has_behaviors": False,
            "has_cursorrules": False
        }
        
        # Check for .cursor/ folder
        cursor_path = project_path / ".cursor"
        if cursor_path.exists() and cursor_path.is_dir():
            findings["has_cursor_folder"] = True
            score += 15
            
            # Check for identity.md
            if (cursor_path / "identity.md").exists():
                findings["has_identity"] = True
                score += 5
            
            # Check for rules.md
            if (cursor_path / "rules.md").exists():
                findings["has_rules"] = True
                score += 5
            
            # Check for behaviors/ folder
            if (cursor_path / "behaviors").exists():
                findings["has_behaviors"] = True
                score += 5
        
        # Check for deprecated .cursorrules
        if (project_path / ".cursorrules").exists():
            findings["has_cursorrules"] = True
            score -= 10  # Penalty for deprecated file
        
        findings["score"] = max(0, score)  # Don't go negative
        return findings
    
    def assess_agent_structure(self, project_path: Path) -> Dict[str, Any]:
        """
        Assess agent structure (30 points max).
        
        Checks for:
        - agents/ folder (10 pts)
        - agents/knowledge-graphs/ (10 pts)
        - agents/skills/ (5 pts)
        - agents/NEW_AGENT_START_HERE.md (5 pts)
        """
        score = 0
        max_score = 30
        findings = {
            "score": 0,
            "max": max_score,
            "has_agents_folder": False,
            "has_knowledge_graphs": False,
            "has_skills": False,
            "has_start_here": False
        }
        
        agents_path = project_path / "agents"
        if agents_path.exists() and agents_path.is_dir():
            findings["has_agents_folder"] = True
            score += 10
            
            # Check for knowledge-graphs/
            if (agents_path / "knowledge-graphs").exists():
                findings["has_knowledge_graphs"] = True
                score += 10
            
            # Check for skills/
            if (agents_path / "skills").exists():
                findings["has_skills"] = True
                score += 5
            
            # Check for NEW_AGENT_START_HERE.md
            if (agents_path / "NEW_AGENT_START_HERE.md").exists():
                findings["has_start_here"] = True
                score += 5
        
        findings["score"] = score
        return findings
    
    def assess_knowledge_graphs(self, project_path: Path) -> Dict[str, Any]:
        """
        Assess knowledge graphs (20 points max).
        
        Checks for:
        - master-graph.json (5 pts)
        - Role-specific KG (5 pts)
        - Skills graph (5 pts)
        - Behaviors graph (5 pts)
        """
        score = 0
        max_score = 20
        findings = {
            "score": 0,
            "max": max_score,
            "has_master_graph": False,
            "has_role_kg": False,
            "has_skills_graph": False,
            "has_behaviors_graph": False
        }
        
        kg_path = project_path / "agents" / "knowledge-graphs"
        if kg_path.exists():
            # Check for master-graph.json
            if (kg_path / "master-graph.json").exists():
                findings["has_master_graph"] = True
                score += 5
            
            # Check for any role-specific KG (*-knowledge-graph.json)
            role_kgs = list(kg_path.glob("*-knowledge-graph.json"))
            if role_kgs:
                findings["has_role_kg"] = True
                score += 5
            
            # Check for skills graph
            skills_graphs = list(kg_path.glob("*-skills-graph.json"))
            if skills_graphs:
                findings["has_skills_graph"] = True
                score += 5
            
            # Check for behaviors graph
            behaviors_graphs = list(kg_path.glob("*-behaviors-graph.json"))
            if behaviors_graphs:
                findings["has_behaviors_graph"] = True
                score += 5
        
        findings["score"] = score
        return findings
    
    def assess_documentation(self, project_path: Path) -> Dict[str, Any]:
        """
        Assess documentation (10 points max).
        
        Checks for:
        - docs/ folder (5 pts)
        - Role-specific docs (5 pts)
        """
        score = 0
        max_score = 10
        findings = {
            "score": 0,
            "max": max_score,
            "has_docs_folder": False,
            "has_role_docs": False
        }
        
        docs_path = project_path / "docs"
        if docs_path.exists() and docs_path.is_dir():
            findings["has_docs_folder"] = True
            score += 5
            
            # Check for role-specific folders (builder/, manager/, etc.)
            role_folders = [d for d in docs_path.iterdir() if d.is_dir()]
            if role_folders:
                findings["has_role_docs"] = True
                score += 5
        
        findings["score"] = score
        return findings
    
    def assess_scripts(self, project_path: Path) -> Dict[str, Any]:
        """
        Assess scripts (10 points max).
        
        Checks for:
        - scripts/ folder (5 pts)
        - Reusable scripts (5 pts)
        """
        score = 0
        max_score = 10
        findings = {
            "score": 0,
            "max": max_score,
            "has_scripts_folder": False,
            "has_reusable_scripts": False
        }
        
        scripts_path = project_path / "scripts"
        if scripts_path.exists() and scripts_path.is_dir():
            findings["has_scripts_folder"] = True
            score += 5
            
            # Check for Python scripts
            py_scripts = list(scripts_path.glob("*.py"))
            if len(py_scripts) >= 2:  # At least 2 reusable scripts
                findings["has_reusable_scripts"] = True
                score += 5
        
        findings["score"] = score
        return findings
    
    def generate_recommendations(self, findings: Dict[str, Any], total_score: int) -> List[str]:
        """Generate actionable recommendations based on findings."""
        recommendations = []
        
        # Configuration issues
        config = findings.get("configuration", {})
        if config.get("has_cursorrules"):
            recommendations.append("CRITICAL: Migrate from .cursorrules to .cursor/ structure")
        if not config.get("has_cursor_folder"):
            recommendations.append("HIGH: Create .cursor/ folder with identity.md and rules.md")
        elif not config.get("has_identity"):
            recommendations.append("HIGH: Add .cursor/identity.md")
        elif not config.get("has_rules"):
            recommendations.append("MEDIUM: Add .cursor/rules.md")
        if not config.get("has_behaviors"):
            recommendations.append("MEDIUM: Create .cursor/behaviors/ folder")
        
        # Agent structure issues
        structure = findings.get("agent_structure", {})
        if not structure.get("has_agents_folder"):
            recommendations.append("HIGH: Implement AgentLoom V3 agent structure (create agents/ folder)")
        elif not structure.get("has_knowledge_graphs"):
            recommendations.append("HIGH: Add agents/knowledge-graphs/ with master-graph.json")
        if not structure.get("has_skills"):
            recommendations.append("MEDIUM: Create agents/skills/ folder")
        if not structure.get("has_start_here"):
            recommendations.append("MEDIUM: Add agents/NEW_AGENT_START_HERE.md")
        
        # Knowledge graph issues
        kg = findings.get("knowledge_graphs", {})
        if kg.get("score", 0) < 15:
            recommendations.append("MEDIUM: Complete knowledge graph implementation")
        
        # Documentation issues
        docs = findings.get("documentation", {})
        if not docs.get("has_docs_folder"):
            recommendations.append("LOW: Create docs/ folder for documentation")
        
        # Scripts issues
        scripts = findings.get("scripts", {})
        if not scripts.get("has_scripts_folder"):
            recommendations.append("LOW: Create scripts/ folder for automation")
        
        # If no issues, add positive note
        if not recommendations and total_score >= 90:
            recommendations.append("✅ Project is fully compliant with AgentLoom V3")
        
        return recommendations
    
    def determine_migration_priority(self, total_score: int, has_cursorrules: bool) -> str:
        """Determine migration priority based on score and deprecated features."""
        if has_cursorrules:
            return "high"  # Deprecated features always high priority
        elif total_score < 50:
            return "high"
        elif total_score < 70:
            return "medium"
        else:
            return "low"
    
    def get_compliance_level(self, total_score: int) -> tuple[str, str]:
        """Get compliance level and status emoji."""
        if total_score >= 90:
            return "Full V3 Compliance", "✅"
        elif total_score >= 70:
            return "Partial V3 Compliance", "⚠️"
        elif total_score >= 50:
            return "Legacy Structure", "🔄"
        else:
            return "No Agent Structure", "❌"
    
    def assess_project(self, project: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Assess a single project for AgentLoom V3 compliance."""
        project_id = project.get("id")
        project_path_str = project.get("path")
        
        if not project_id or not project_path_str:
            return None
        
        # Skip special cases
        if project_id.lower() in [s.lower() for s in SPECIAL_CASES]:
            return None
        
        project_path = self.projects_root / project_path_str
        
        if not project_path.exists():
            return {
                "id": project_id,
                "name": project.get("name", project_id),
                "category": project.get("category", "unknown"),
                "compliance_score": 0,
                "compliance_level": "Project Not Found",
                "status": "❓",
                "error": f"Project directory not found: {project_path}"
            }
        
        # Run all assessments
        config_findings = self.assess_configuration(project_path)
        structure_findings = self.assess_agent_structure(project_path)
        kg_findings = self.assess_knowledge_graphs(project_path)
        docs_findings = self.assess_documentation(project_path)
        scripts_findings = self.assess_scripts(project_path)
        
        # Calculate total score
        total_score = (
            config_findings["score"] +
            structure_findings["score"] +
            kg_findings["score"] +
            docs_findings["score"] +
            scripts_findings["score"]
        )
        
        # Compile findings
        findings = {
            "configuration": config_findings,
            "agent_structure": structure_findings,
            "knowledge_graphs": kg_findings,
            "documentation": docs_findings,
            "scripts": scripts_findings
        }
        
        # Generate recommendations
        recommendations = self.generate_recommendations(findings, total_score)
        
        # Determine compliance level and priority
        compliance_level, status = self.get_compliance_level(total_score)
        migration_priority = self.determine_migration_priority(
            total_score,
            config_findings.get("has_cursorrules", False)
        )
        
        return {
            "id": project_id,
            "name": project.get("name", project_id),
            "category": project.get("category", "unknown"),
            "compliance_score": total_score,
            "compliance_level": compliance_level,
            "status": status,
            "findings": findings,
            "recommendations": recommendations,
            "migration_priority": migration_priority
        }
    
    def assess_all(self, project_filter: Optional[str] = None) -> Dict[str, Any]:
        """Assess all projects or a specific project."""
        print("Loading projects metadata...")
        metadata = self.load_metadata()
        
        projects = metadata.get("projects", [])
        
        # Filter out special cases
        projects = [p for p in projects if p.get("id", "").lower() not in [s.lower() for s in SPECIAL_CASES]]
        
        if project_filter:
            projects = [p for p in projects if p.get("id") == project_filter]
            if not projects:
                raise ValueError(f"Project not found: {project_filter}")
        
        total_projects = len(projects)
        print(f"Assessing {total_projects} agent project(s)...")
        print(f"Excluding {len(SPECIAL_CASES)} special case projects")
        print("-" * 80)
        
        for idx, project in enumerate(projects, 1):
            project_id = project.get("id", "unknown")
            print(f"[{idx}/{total_projects}] {project_id:40} ", end="", flush=True)
            
            assessment = self.assess_project(project)
            
            if assessment:
                self.assessments.append(assessment)
                score = assessment.get("compliance_score", 0)
                status = assessment.get("status", "?")
                print(f"{status} {score}/100")
            else:
                print("- (skipped)")
        
        print("-" * 80)
        
        # Generate summary
        summary = self._generate_summary()
        
        # Create report
        report = {
            "timestamp": datetime.now().isoformat(),
            "agentloom_version": "3.0.0",
            "total_projects_assessed": total_projects,
            "summary": summary,
            "projects": self.assessments,
            "migration_priorities": self._get_migration_priorities(),
            "deprecated_features": self._get_deprecated_features()
        }
        
        return report
    
    def _generate_summary(self) -> Dict[str, Any]:
        """Generate summary statistics."""
        full_compliance = sum(1 for a in self.assessments if a.get("compliance_score", 0) >= 90)
        partial_compliance = sum(1 for a in self.assessments if 70 <= a.get("compliance_score", 0) < 90)
        legacy_structure = sum(1 for a in self.assessments if 50 <= a.get("compliance_score", 0) < 70)
        no_structure = sum(1 for a in self.assessments if a.get("compliance_score", 0) < 50)
        
        avg_score = sum(a.get("compliance_score", 0) for a in self.assessments) / len(self.assessments) if self.assessments else 0
        
        return {
            "full_compliance": full_compliance,
            "partial_compliance": partial_compliance,
            "legacy_structure": legacy_structure,
            "no_structure": no_structure,
            "average_score": round(avg_score, 1)
        }
    
    def _get_migration_priorities(self) -> Dict[str, List[str]]:
        """Get projects grouped by migration priority."""
        priorities = {"high": [], "medium": [], "low": []}
        
        for assessment in self.assessments:
            priority = assessment.get("migration_priority", "medium")
            project_id = assessment.get("id")
            if project_id:
                priorities[priority].append(project_id)
        
        return priorities
    
    def _get_deprecated_features(self) -> Dict[str, List[str]]:
        """Get projects with deprecated features."""
        cursorrules_files = []
        
        for assessment in self.assessments:
            config = assessment.get("findings", {}).get("configuration", {})
            if config.get("has_cursorrules"):
                cursorrules_files.append(assessment.get("id"))
        
        return {
            "cursorrules_files": cursorrules_files
        }
    
    def save_report(self, report: Dict[str, Any]) -> Path:
        """Save compliance report to temp directory."""
        temp_dir = Path(__file__).parent.parent / "temp"
        temp_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = temp_dir / f"agentloom_compliance_report_{timestamp}.json"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Assess AgentLoom V3 compliance")
    parser.add_argument("--project", type=str, help="Assess specific project ID")
    parser.add_argument("--projects-root", type=str, help="Path to projects root directory")
    
    args = parser.parse_args()
    
    # Determine projects root
    if args.projects_root:
        projects_root = Path(args.projects_root)
    else:
        # Default: assume script is in Agentic-AI-Proj-manager/scripts/
        script_dir = Path(__file__).parent
        projects_root = script_dir.parent.parent
    
    if not projects_root.exists():
        print(f"Error: Projects root directory not found: {projects_root}")
        sys.exit(1)
    
    print(f"Projects root: {projects_root}")
    print()
    
    # Create assessor and run
    assessor = AgentLoomAssessor(projects_root=projects_root)
    
    try:
        report = assessor.assess_all(project_filter=args.project)
        report_path = assessor.save_report(report)
        
        print()
        print("=" * 80)
        print("COMPLIANCE ASSESSMENT SUMMARY")
        print("=" * 80)
        print(f"Total projects assessed: {report['total_projects_assessed']}")
        print(f"AgentLoom version: {report['agentloom_version']}")
        print()
        print("Compliance Levels:")
        print(f"  ✅ Full Compliance (90-100):    {report['summary']['full_compliance']}")
        print(f"  ⚠️  Partial Compliance (70-89):  {report['summary']['partial_compliance']}")
        print(f"  🔄 Legacy Structure (50-69):    {report['summary']['legacy_structure']}")
        print(f"  ❌ No Structure (0-49):         {report['summary']['no_structure']}")
        print()
        print(f"Average Score: {report['summary']['average_score']}/100")
        print()
        print("Migration Priorities:")
        print(f"  High:   {len(report['migration_priorities']['high'])} projects")
        print(f"  Medium: {len(report['migration_priorities']['medium'])} projects")
        print(f"  Low:    {len(report['migration_priorities']['low'])} projects")
        
        if report['deprecated_features']['cursorrules_files']:
            print()
            print(f"⚠️  Deprecated .cursorrules files found in {len(report['deprecated_features']['cursorrules_files'])} projects")
        
        print()
        print(f"Report saved to: {report_path}")
        print("=" * 80)
        
        sys.exit(0)
    
    except Exception as e:
        print(f"\nFatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
