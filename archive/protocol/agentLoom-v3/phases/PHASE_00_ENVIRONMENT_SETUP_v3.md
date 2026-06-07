# Phase 0: Environment Setup

**AI Agent Setup Protocol V3.0**

---

## Objective

Verify environment prerequisites and prepare workspace before starting the protocol.

---

## Requirements

### Required

**Python 3.9+**

- Used for validation scripts, KG operations, and pattern extraction
- Requires virtual environment for dependency isolation
- Check version: `python --version` or `python3 --version`

### Optional

**Git** (recommended)

- For version control and tracking changes
- Not required for protocol execution

---

## Setup Steps

### Step 1: Verify Python Installation

**Check Python version**:

```powershell
python --version
# or
python3 --version
```

**Expected**: Python 3.9.0 or higher

**If not installed**: Download from [python.org](https://www.python.org/downloads/)

---

### Step 2: Create Python Virtual Environment

> **IMPORTANT**: This step should be done by the **human user** before starting the protocol.
> The AI agent will verify the setup but cannot reliably create the venv due to system-level requirements.

**One-Time Setup (Human User)**:

```powershell
# 1. Navigate to project root
cd path\to\my-agent-project

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify installation
python -c "import json; print('✅ Python environment ready!')"
```

**Troubleshooting**:

If you get `Activate.ps1 cannot be loaded because running scripts is disabled`:

```powershell
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Daily Usage**:

```powershell
# Activate virtual environment (do this each time you open a new terminal)
.venv\Scripts\Activate.ps1

# You should see (.venv) in your terminal prompt
```

---

### Step 3: AI Agent Verification (Automated)

**The AI agent will verify the environment is ready**:

```powershell
# Agent will run these checks:

# 1. Check if .venv exists
Test-Path .venv

# 2. Verify Python in venv
.venv\Scripts\python.exe --version

# 3. Check if dependencies are installed
.venv\Scripts\python.exe -c "import jsonschema; print('✅ Dependencies installed')"

# 4. Test validation script
.venv\Scripts\python.exe scripts/validate_kg_links.py --help
```

**Agent Instructions**:

When executing this phase, the agent should:

1. Check if `.venv/` directory exists
2. If not, **STOP** and ask user to create it (provide instructions above)
3. If exists, verify dependencies are installed
4. If dependencies missing, **STOP** and ask user to run `pip install -r requirements.txt`
5. Once verified, proceed to create project structure

---

### Step 4: Create Your Project Structure

**Create your project root directory**:

```powershell
mkdir my-agent-project
cd my-agent-project
```

**Create your content folder** (where your domain-specific content will live):

```powershell
mkdir content-raw
```

---

### Step 5: Copy the Protocol Package

**Copy the entire `agentLoom` folder** into your project root:

```
my-agent-project/
├── .venv/                          (Python virtual environment - you create this)
├── requirements.txt                (Python dependencies)
├── content-raw/                    (your domain content - you create this)
└── agentLoom/                      (protocol package - you copy this)
    ├── builder-assets/             (foundation components)
    ├── examples/                   (reference templates)
    ├── phases/                     (protocol instructions)
    ├── specs/                      (technical specifications)
    ├── outputs/                    (phase outputs will go here)
    └── V3_DESIGN_SUMMARY.md
```

**Important**: The protocol package should be at the **same level** as your `content-raw/` folder, not inside it.

---

### Step 6: Verify Package Structure

**Check that `agentLoom/` contains**:

```
agentLoom/
├── builder-assets/
│   ├── .cursor/behaviors/          (core + builder behaviors)
│   ├── agents/
│   │   ├── knowledge-graphs/       (builder-*.json files)
│   │   ├── skills/system/          (system skills)
│   │   └── visualization-dynamic.html
│   ├── docs/general/               (general documentation)
│   └── scripts/                    (validation scripts)
├── examples/                       (reference templates)
├── phases/                         (9 phase instruction files)
├── specs/                          (technical specifications)
└── outputs/                        (empty - will be populated during execution)
```

---

### Step 7: Test Python Scripts (Agent Verification)

**Agent will verify scripts can run**:

```powershell
# Activate venv and test
.venv\Scripts\Activate.ps1
python agentLoom/builder-assets/scripts/validate_structure.py
```

**Expected**: Script runs (may show errors about missing structure - that's normal at this stage)

---

## Environment Checklist

Before proceeding to Phase 1, confirm:

### Human User Checklist

- [ ] Python 3.9+ installed and accessible
- [ ] Virtual environment created (`.venv/`)
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Project root directory created (`my-agent-project/`)
- [ ] Content folder created (`content-raw/`)

### AI Agent Checklist (Automated Verification)

- [ ] `.venv/` directory exists
- [ ] Python accessible in venv (`.venv/Scripts/python.exe`)
- [ ] Dependencies installed (jsonschema, etc.)
- [ ] Protocol package copied (`agentLoom/`)
- [ ] Package structure verified (builder-assets, phases, specs, examples present)
- [ ] Write permissions in project directory
- [ ] Validation scripts executable

---

## Agent Execution Pattern

**When AI agent starts Phase 0, it should**:

```markdown
1. CHECK: Does .venv/ exist?
   - NO → STOP and provide setup instructions to user
   - YES → Continue

2. CHECK: Are dependencies installed?
   - Run: .venv\Scripts\python.exe -c "import jsonschema"
   - FAIL → STOP and ask user to run: pip install -r requirements.txt
   - SUCCESS → Continue

3. VERIFY: Project structure
   - Check content-raw/ exists
   - Check agentLoom/ exists
   - Check write permissions

4. TEST: Run validation script
   - .venv\Scripts\python.exe scripts/validate_structure.py

5. REPORT: Environment status to user
   - ✅ All checks passed → Proceed to Phase 1
   - ❌ Any check failed → Provide specific fix instructions
```

---

## Troubleshooting

### Python not found

**Windows**: Add Python to PATH during installation, or use `py` command  
**macOS/Linux**: Use `python3` instead of `python`

### Virtual environment activation fails

**PowerShell Execution Policy**:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ModuleNotFoundError when running scripts

**Solution**: Ensure venv is activated and dependencies installed:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Permission errors

**Solution**: Choose a different project location where you have write access

### Protocol package missing folders

**Solution**: Re-download the complete `agentLoom` package

---

## Completion

```
✅ Phase 0 Complete

Python: [version]
Virtual Environment: ✅ Created and activated (.venv/)
Dependencies: ✅ Installed
Project Root: [path]
Content Folder: ✅ Created (content-raw/)
Protocol Package: ✅ Copied (agentLoom/)

Ready to proceed to Phase 1!
```

---

## Daily Workflow Reminder

**Each time you start working**:

```powershell
# 1. Navigate to project
cd path\to\my-agent-project

# 2. Activate virtual environment
.venv\Scripts\Activate.ps1

# 3. Verify activation (you should see (.venv) in prompt)

# 4. Start working with AI agent
```

**When done**:

```powershell
# Deactivate virtual environment
deactivate
```

---

**Next**: [Phase 1: Information Discovery](PHASE_01_INFORMATION_DISCOVERY_v3.md)
