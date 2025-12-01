# NEW_AGENT_START_HERE.md

# Agent Initialization Script (Executed by the Agent Itself)

Hello Agent — this is your startup script.

Follow all steps below **automatically**, without asking the user to perform any action.

---

## Step 1 — Load Identity

Read:
@.cursor/identity.md

Purpose:

- Understand your name, purpose, boundaries, and the two roles you support.

---

## Step 2 — Load Core Knowledge (Master Graph)

Read and analyze:
@agents/knowledge-graphs/master-graph.json

Purpose:

- Learn the high-level structure.
- Locate role-specific sub-graphs.
- Locate project graph.
- Locate behaviors and skills graphs.

---

## Step 3 — Ask User for Role Selection

Ask:
“Which role should I activate: Agent Builder or Project Manager?”

Wait for user choice.

---

## Step 4 — Load Role-Specific Knowledge Graphs

If user selects Builder:
    Read:
    - @agents/knowledge-graphs/builder-knowledge-graph.json
    - @agents/knowledge-graphs/builder-skills-graph.json
    - @agents/knowledge-graphs/builder-behaviors-graph.json

If user selects Manager:
    Read:
    - @agents/knowledge-graphs/manager-knowledge-graph.json
    - @agents/knowledge-graphs/manager-skills-graph.json
    - @agents/knowledge-graphs/manager-behaviors-graph.json

Both roles also load:
    - @agents/knowledge-graphs/project-graph.json

---

## Step 5 — Load Behaviors

Load all behaviors by reading all files under:
@.cursor/behaviors/

(These define your safety, confidentiality, and workflow rules.)

---

## Step 6 — Internalize Operational Boundaries

**CRITICAL**: You must adhere to these rules at all times.

### What NOT to Touch

**Never modify without specific instruction**:

- `.cursor/project-registry.json` (use `skill-update-registry` instead)
- `agents/knowledge-graphs/*.json` (use `skill-kg-update-node` instead)
- `scripts/validate_*.py` (unless fixing bugs)

**Read-only for most tasks**:

- All `.md` files (read for context)
- All JSON files (read for navigation)

### What You Can Freely Access

**Always OK to read**:

- Any `.md` file in the system
- Any JSON file (for information, not modification)
- `visualization.html` (open in browser)
- Project folders (respecting confidentiality)

**OK to create**:

- New `.md` files in `docs/` following CONTENT_TEMPLATE.md
- New behavior files in `.cursor/behaviors/` (with proper indexing)
- New skill files in `agents/skills/` (with proper indexing)
- Temporary files in `temp/`

### File Structure Reference

```text
Agentic-AI-Proj-manager/
├── .cursor/                  # System configuration (auto-loaded by Cursor)
│   ├── identity.md           # Agent identity & roles
│   ├── rules.md              # Behavior index (lightweight)
│   ├── behaviors/            # Protocol definitions
│   ├── project-registry.json # Project tracking database
│   └── templates/            # Content templates
│
├── agents/                   # Agent logic & "brain"
│   ├── knowledge-graphs/     # KG JSON files
│   ├── skills/               # Skill definitions
│   ├── NEW_AGENT_START_HERE.md     # This file
│   └── USER_MANUAL_CURSOR.md       # User Prompts
│
├── docs/                     # Documentation organized by role
├── scripts/                  # Automation & validation tools
├── public/                   # Public/open-source projects
├── personal/                 # Personal research projects
├── work/                     # Confidential client work
└── temp/                     # Temporary files, tests, backups
```

---

## Step 7 — Confirm Ready

Output the following:

“✅ System Ready.
Role: [ROLE]
Knowledge Loaded: [X] KG nodes
Behaviors Loaded: [Y]
Skills Available: [Z]
How can I help you today?”

---

You are now ready to work.

---

## Appendix: Agent Reference Card

### 5-Minute Cold Start Checklist

- [ ] Load `.cursor/identity.md`
- [ ] Load `agents/knowledge-graphs/master-graph.json`
- [ ] Ask user for role (Builder or Manager)
- [ ] Load 3 role-specific graphs
- [ ] Load `project-graph.json`
- [ ] Confirm operational with summary

### Key Node IDs (Bookmarks)

**System**:

- `sys:root` - System architecture root
- `sys:docs` - Documentation root
- `sys:kg:architecture` - KG meta-structure

**Projects**:

- `proj:root` - All managed projects
- `cat:public` - Public projects folder
- `cat:personal` - Personal projects folder
- `cat:work` - Work projects folder

**Skills**:

- `skill:builder:root` - Builder capabilities root
- `skill-maintain-kg` - KG maintenance orchestrator

**Behaviors**:

- `behavior:core:safety` - System safety protocol
- `behavior:core:confidentiality` - Data separation rules

### Common Commands

**Validation**:

```bash
python scripts/validate_structure.py
python scripts/validate_graphs.py
```

**Visualization**:
Open `agents/knowledge-graphs/visualization.html` in browser

**Git**:

```bash
git status
git add -A
git commit -m "message"
git push
```

### First Tasks by Role

**If Agent Builder**:

1. Run validators: `python scripts/validate_structure.py` and `validate_graphs.py`
2. Open visualization.html → check Unified Brain
3. Report system health to user

**If Project Manager**:

1. Check dashboard: Read `docs/manager/dashboard.md`
2. Ask user: "Any project updates to record?"
3. Be ready to scan repos or generate insights

These are common "first tasks" after cold-start.

### Emergency: Lost Context

If you're confused about where you are or what to do:

1. Re-read `.cursor/identity.md` (who you are)
2. Ask user: "Which role should I be in? What task?"
3. Load relevant graphs for that role
4. Check `docs/manager/dashboard.md` or `docs/builder/plan/` for context
5. Proceed with clarity
