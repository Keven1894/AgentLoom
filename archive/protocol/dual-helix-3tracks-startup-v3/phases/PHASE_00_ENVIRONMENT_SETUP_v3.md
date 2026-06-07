# Phase 0: Environment Setup

**AI Agent Setup Protocol V3.0**

---

## Objective

Verify environment prerequisites and prepare workspace before starting the protocol.

---

## Requirements

### Required

**Python 3.9+**

- Used for validation scripts and local HTTP server
- All scripts use Python standard library only (no pip installs needed)
- Check version: `python --version` or `python3 --version`

### Optional

**Git** (recommended)

- For version control and tracking changes
- Not required for protocol execution

---

## Setup Steps

### Step 1: Verify Python Installation

**Check Python version**:

```bash
python --version
# or
python3 --version
```

**Expected**: Python 3.9.0 or higher

**If not installed**: Download from [python.org](https://www.python.org/downloads/)

### Step 2: Create Your Project Structure

**Create your project root directory**:

```bash
mkdir my-agent-project
cd my-agent-project
```

**Create your content folder** (where your domain-specific content will live):

```bash
mkdir content-raw
```

### Step 3: Copy the Protocol Package

**Copy the entire `dual-helix-3tracks-startup-v3` folder** into your project root:

```
my-agent-project/
├── content-raw/                    (your domain content - you create this)
└── dual-helix-3tracks-startup-v3/  (protocol package - you copy this)
    ├── builder-assets/             (foundation components)
    ├── examples/                   (reference templates)
    ├── phases/                     (protocol instructions)
    ├── specs/                      (technical specifications)
    ├── outputs/                    (phase outputs will go here)
    └── V3_DESIGN_SUMMARY.md
```

**Important**: The protocol package should be at the **same level** as your `content-raw/` folder, not inside it.

### Step 4: Verify Package Structure

**Check that `dual-helix-3tracks-startup-v3/` contains**:

```
dual-helix-3tracks-startup-v3/
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

### Step 5: Test Python Scripts (Optional)

**Verify scripts can run**:

```bash
python dual-helix-3tracks-startup-v3/builder-assets/scripts/validate_structure.py
```

**Expected**: Script runs (may show errors about missing structure - that's normal at this stage)

---

## Environment Checklist

Before proceeding to Phase 1, confirm:

- [ ] Python 3.9+ installed and accessible
- [ ] Project root directory created (`my-agent-project/`)
- [ ] Content folder created (`content-raw/`)
- [ ] Protocol package copied (`dual-helix-3tracks-startup-v3/`)
- [ ] Package structure verified (builder-assets, phases, specs, examples present)
- [ ] Write permissions in project directory
- [ ] (Optional) Git initialized for version control

---

## Troubleshooting

### Python not found

**Windows**: Add Python to PATH during installation, or use `py` command  
**macOS/Linux**: Use `python3` instead of `python`

### Permission errors

**Solution**: Choose a different project location where you have write access

### Protocol package missing folders

**Solution**: Re-download the complete `dual-helix-3tracks-startup-v3` package

---

## Completion

```
✅ Phase 0 Complete

Python: [version]
Project Root: [path]
Content Folder: ✅ Created (content-raw/)
Protocol Package: ✅ Copied (dual-helix-3tracks-startup-v3/)

Ready to proceed to Phase 1!
```

---

**Next**: [Phase 1: Information Discovery](PHASE_01_INFORMATION_DISCOVERY_v3.md)
