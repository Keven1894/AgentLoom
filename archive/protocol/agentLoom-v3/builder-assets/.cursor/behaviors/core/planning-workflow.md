---
description: Plan-first workflow - always create plans before implementation
version: 1.0
alwaysApply: true
priority: high
category: workflows
tags: ["planning", "workflow", "discipline"]
lastUpdated: 2025-11-30
author: Manager Agent
---

# Planning Workflow

## 🎯 Critical Rule: Plan First, Implement Later

**Before ANY non-trivial work:**

1. ❌ Do NOT start implementation immediately
2. ✅ Create plan in `docs/plan/todo/`
3. ✅ Get approval
4. ✅ Then implement

---

## The 4-Step Process

### Step 1: Create Plan

- Location: `docs/plan/todo/[plan-name].md`
- Template: `docs/plan/plan-template.md`
- Include: Objective, steps, outcomes, risks

### Step 2: Get Approval

- Present plan for review
- Wait for approval
- Adjust based on feedback

### Step 3: Implement

- Follow plan systematically
- Track progress
- Document deviations

### Step 4: Complete & Summarize

- Move to `docs/plan/complete/`
- Create `[plan-name]_sum-log.md`
- Document: accomplishments, changes, lessons

---

## When to Create Plans

**Always plan for:**

- ✅ New skills or capabilities
- ✅ Major refactoring
- ✅ Architecture changes
- ✅ Complex analysis tasks
- ✅ Multi-step workflows
- ✅ Major knowledge graph updates

**Optional for:**

- Minor documentation fixes
- Simple configuration changes
- Very small changes

---

## Quick Reference

**File locations:**

- Active: `docs/plan/todo/`
- Complete: `docs/plan/complete/`
- Summaries: `docs/plan/complete/[name]_sum-log.md`

**Naming:** `YYYY-MM-DD-description.md` or `feature-name.md`

---

## Detailed Implementation

This core rule is implemented via the **AgentLoom Development Lifecycle**.

- [Development Lifecycle Guide](./development-lifecycle/INDEX.md)
- [Phase 1: Planning](./development-lifecycle/phase-1-planning.md)

**Remember: Plan discipline prevents chaos!**
