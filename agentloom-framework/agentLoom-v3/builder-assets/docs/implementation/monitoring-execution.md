---
type: knowledge
category: monitoring
id: monitoring-execution
---

# Monitoring Strategy: Execution & Tools


## 📊 Monitoring Workflow

### Daily Quick Check (5 min)

```bash

## 🛠️ Tools to Create (Future)

### Tool 1: Project Change Monitor

**Script:** `manager-tools/check-project-updates.py`

**Function:**
```python
def check_project_updates():
    """
    Check all 13 projects for updates since last extraction.
    
    Returns:
    - Projects with new commits
    - Files changed counts
    - Last extraction dates
    - Days since extraction
    - Recommended action (Review/Skip)
    """
```

**Output:**
```
PROJECT STATUS REPORT - 2025-11-12
=====================================

WORK PROJECTS:
- DIVA: 5 commits (7 days) → REVIEW (new feature detected)
- FIU Platform: 2 commits (3 days) → SKIP (bug fixes)
- EnviStor Data: 0 commits → OK
...

PERSONAL PROJECTS:
- Tax Assistant: 1 commit (30 days) → SKIP (config change)
...

PUBLIC PROJECTS:
- Research Roadmap: 12 commits (5 days) → REVIEW (new case study)
- co-agenticOS: 3 commits (2 days) → SKIP (docs updated)

RECOMMENDATIONS:
- Review: DIVA, Research Roadmap
- Skip: 11 projects
```

### Tool 2: Partial Extraction Updater

**Script:** `manager-tools/update-dossier.py`

**Function:**
```python
def update_dossier(project, dossier_number, reason):
    """
    Update a specific dossier for a project.
    
    Args:
    - project: Project name
    - dossier_number: Which dossier (00, 01, etc.)
    - reason: Why updating
    
    Actions:
    - Regenerate specified dossier
    - Update manifest (note partial update)
    - Sync to research repos
    - Update dashboard
    """
```

**Usage:**
```bash

## 📊 Tracking System

### Extraction Metadata (Add to Each Project)

**File:** `[category]/[project]/extraction/EXTRACTION-METADATA.json`

```json
{
  "project_name": "fiugis-agent-platform",
  "extraction_version": "1.0",
  "initial_extraction_date": "2025-11-12",
  "last_updated": "2025-11-12",
  "update_history": [
    {
      "date": "2025-11-12",
      "type": "initial",
      "dossiers_updated": "all",
      "reason": "Initial extraction"
    }
  ],
  "source_git_commit": "abc123...",
  "next_review_date": "2025-12-12"
}
```

**Benefits:**
- Track when extracted
- Track what was updated
- Track source commit (for comparison)
- Schedule next review

### Dashboard Enhancement

**Add to each project entry:**
- Last extraction date
- Last review date
- Next review date
- Update frequency needed (daily/weekly/monthly/quarterly)

**Example:**
```markdown
#### FIU Multi-Agent Platform ⭐
- **Extracted:** 2025-11-12 (v1.0)
- **Last Review:** 2025-11-12
- **Next Review:** 2025-12-12 (monthly)
- **Update Frequency:** Monthly (active development)
- **Source Commit:** abc123...
```

---


## 💻 Automation Opportunities

### Level 1: Automated Detection (Easy)

**Create:** `manager-tools/daily-check.py`

**What it does:**
```bash

## 🔧 Specific Project Monitoring Strategies

### High-Velocity Projects (Weekly Updates)

**Projects:** FIU Platform, EnviStor Dev, Fiugis Dev Agent

**Why:** Active development, frequent changes, high research value

**Strategy:**
- Weekly review mandatory
- Partial updates common
- Full re-extraction quarterly

### Medium-Velocity Projects (Monthly Updates)

**Projects:** EnviStor Data, AI Scholar, DIVA

**Why:** Moderate changes, stable features

**Strategy:**
- Monthly review
- Partial updates as needed
- Full re-extraction semi-annually

### Low-Velocity Projects (Quarterly Updates)

**Projects:** Personal projects (Tax, CompAssist, SavvyShop, AI Coach)

**Why:** Stable, infrequent changes

**Strategy:**
- Quarterly review
- Updates rare
- Full re-extraction annually (or when major changes)

### Framework Projects (Event-Driven)

**Projects:** Research Roadmap, co-agenticOS

**Why:** They receive our extractions, update based on them

**Strategy:**
- Monitor when they integrate our content
- Re-extract when major framework updates
- Version-driven (when DOI version changes)

---


## 📝 Update Documentation Standard

### When Updating an Extraction

**Always document:**

**1. Update EXTRACTION-METADATA.json:**
```json
{
  "update_history": [
    {
      "date": "2025-12-15",
      "type": "partial",
      "dossiers_updated": ["02"],
      "reason": "New agent added to platform",
      "source_commit": "def456..."
    }
  ]
}
```

**2. Update EXTRACTION-MANIFEST.md:**
```markdown