# 📝 Drafts Directory

This directory contains research paper drafts and publication materials at various stages of development.

## 🔄 Dual Repository Strategy

This project uses **two repositories**:
- **GitHub (Public)**: Framework and methodology - excludes `private/` folders
- **GitLab (Full)**: Complete materials including `private/` folders

See [`../DUAL_REPO_STRATEGY.md`](../DUAL_REPO_STRATEGY.md) for details.

## 🗂️ Directory Structure

```
drafts/
├── public/              # ✅ Visible on both GitHub and GitLab
│   ├── diva-publication-roadmap.md
│   ├── workshop-paper-outline.md
│   └── REVIEW_FEEDBACK_ACTION_PLAN.md
│
└── private/             # 🔒 GitLab only (excluded from GitHub)
    ├── diva-workshop-paper.md          [full draft, ~7,200 words]
    └── USER_INPUT_NEEDED.md            [sensitive project data]
```

---

## 🔒 Privacy & IP Protection

### ✅ **Public Drafts** (`public/`)

**Visible on**: GitHub + GitLab

**Content**:
- Research planning and publication strategies
- Paper outlines and structural frameworks  
- Academic workflow demonstrations
- High-level conceptual materials

**Restrictions**: No quantitative results, specific metrics, or proprietary configurations

---

### 🔒 **Private Drafts** (`private/`)

**Visible on**: GitLab only (excluded from GitHub via `.gitignore`)

**Content**: Materials requiring confidentiality until formal publication:

| File | Reason for Privacy |
|------|-------------------|
| `diva-workshop-paper.md` | Complete 7,200-word paper draft with full experimental data (50+ deployments, ROI metrics, etc.). Early public release may be considered "preprint" by some conferences (IEEE, SCITEPRESS) and cause rejection. |
| `USER_INPUT_NEEDED.md` | Original raw data from EnviStor project including performance metrics, governance rules, and system architecture details. |

**Why GitLab-only?**
- **Prevents preprint conflicts**: Many conferences reject publicly available submissions
- **Protects IP priority**: Quantitative results need embargo until acceptance
- **Controlled access**: GitLab permissions manage who sees complete data
- **Version control**: Full Git history maintained in private repository

---

## 📦 Publication Workflow

### Pre-submission Phase
```
[GitLab Draft] → [Internal Review] → [Refinement] → [Submission]
      ↓                                                 ↑
 private/                                    (stays on GitLab only)
```

### Post-acceptance Phase
```
[Accepted] → [Camera-ready] → [Published] → [Move to public/]
                                                   ↓
                                        Now visible on GitHub
                                        (with DOI & citations)
```

---

## 🚀 Release Strategy

### During Development
- Work in GitLab repository (full access to all materials)
- Keep sensitive content in `private/` folders
- Push to both GitHub and GitLab (GitHub auto-excludes private/)

### After Acceptance
1. Move content from `private/` to `public/`
2. Add DOI and publication metadata
3. Push to both repositories
4. Now visible on GitHub

### Optional: Zenodo Archival
- Upload accepted version to Zenodo for permanent DOI
- Link to both GitHub (public) and GitLab (full) repositories

---

## 📋 Verification of Originality

Your authorship is protected through:

1. **GitLab Repository**: Full Git history with timestamps (private access)
2. **GitHub Repository**: Public commits show framework development
3. **Zenodo DOI**: Early versions registered with permanent identifier (optional)
4. **Submission Records**: Conference/journal confirmations and correspondence

---

## 🔄 Moving Files Between Categories

### Making a Private Draft Public
```powershell
# After acceptance/publication (in GitLab clone)
Move-Item drafts/private/paper-name.md drafts/public/
git add drafts/public/paper-name.md
git commit -m "docs: publish accepted paper draft"
git push origin main  # GitLab
git push github main  # GitHub (now visible)
```

### Keeping New Sensitive Content Private
```powershell
# Create in private/ directory (in GitLab clone)
New-Item drafts/private/new-confidential-draft.md
git add drafts/private/new-confidential-draft.md
git commit -m "docs: add new private draft"
git push origin main  # GitLab only
# Don't push to GitHub or it auto-excludes anyway
```

---

## ⚠️ Important Notes

1. **Use GitLab for private content**: All `private/` folders are managed there
2. **GitHub auto-excludes**: `.gitignore` prevents `private/` from reaching GitHub
3. **Backup strategy**: GitLab serves as primary backup with access control
4. **Collaboration**: 
   - **Full access**: Grant GitLab repository permissions
   - **Public only**: Share GitHub repository link

---

## 📚 Related Documentation

- [Main Research Roadmap](../docs/Agentic-AI-Research-Roadmap.md)
- [Publication Timeline](../docs/Research-Timeline-2025-2027.md)
- [Zenodo Integration Guide](../docs/ZENODO_INTEGRATION.md)
- [Citation Guidelines](../CITATION.cff)

---

## 🤝 Questions?

For questions about publication policies or IP protection:
- Review your institution's research policies
- Check conference/journal preprint policies
- Consult with your research advisor or legal office

---

**Last Updated**: November 10, 2025  
**Maintained by**: Agentic AI Research Lab

