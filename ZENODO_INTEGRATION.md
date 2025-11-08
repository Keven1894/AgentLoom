# Zenodo Integration Guide

This guide explains how to integrate this repository with Zenodo to obtain a permanent DOI (Digital Object Identifier) for academic citation.

## Why Zenodo?

- **Permanent DOI:** Creates a citable, permanent reference
- **Timestamped:** Establishes priority and precedence for your work
- **Academic Recognition:** Widely recognized in research communities
- **Version Control:** Track releases and iterations

## Setup Instructions

### Step 1: Create Zenodo Account

1. Go to [Zenodo.org](https://zenodo.org/)
2. Sign up or log in (can use GitHub OAuth)
3. Verify your email address

### Step 2: Link GitHub Repository

1. Go to Zenodo → Settings → [GitHub](https://zenodo.org/account/settings/github/)
2. Click "Sync now" to fetch your repositories
3. Find `agentic-ai-lab` in the list
4. Toggle the switch to **ON** to enable Zenodo integration

### Step 3: Create First Release

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `Agentic-AI Engineering Framework v1.0 - Initial Release`
5. Description:
   ```markdown
   First public release of the Agentic-AI Engineering Framework
   
   ## Highlights
   - Complete framework documentation (Context → Doc → Index → RAG → Fine-tune)
   - Research roadmap and timeline (2025-2027)
   - Workshop paper outline
   - Getting started guide with code examples
   
   ## Citation
   See CITATION.cff for citation details
   ```
6. Click "Publish release"

### Step 4: Get Your DOI

1. Zenodo will automatically detect the release
2. Go to Zenodo → Upload → GitHub
3. Find your new deposit
4. Copy the DOI (format: `10.5281/zenodo.XXXXXXX`)

### Step 5: Update Repository

Update the following files with your DOI:

**CITATION.cff:**
```yaml
doi: "10.5281/zenodo.XXXXXXX"
```

**README.md** (add badge after other badges):
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

**Paper citations:**
```bibtex
@software{guan2025agenticai,
  author       = {Guan, Boyuan (Keven)},
  title        = {Agentic-AI Engineering Framework},
  month        = nov,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

## Version Release Strategy

### For Each Major Milestone

Create a new GitHub release when:
- **v1.0.0** - Initial framework release (Nov 2025)
- **v1.1.0** - After first workshop paper acceptance
- **v2.0.0** - After first case study paper published
- **v2.1.0** - Additional case studies
- **v3.0.0** - Integrative system paper and toolkit release

### Zenodo Benefits

Each release gets:
- Unique DOI for that version
- Concept DOI (always points to latest)
- Permanent archive (even if GitHub goes down)
- Download statistics
- Citation tracking

## Best Practices

1. **Create meaningful releases:** Don't release too frequently
2. **Write good release notes:** Explain what changed
3. **Update metadata:** Keep CITATION.cff current
4. **Tag properly:** Use semantic versioning (MAJOR.MINOR.PATCH)
5. **Include assets:** Ensure all important files are in the release

## Metadata Checklist

Before creating a release, verify:

- [ ] CITATION.cff has correct information
- [ ] README.md has current author info
- [ ] LICENSE file is present
- [ ] All documentation is up to date
- [ ] No sensitive data or credentials in repository
- [ ] .gitignore properly configured

## Zenodo Record Enhancement

After creating the DOI, enhance your Zenodo record:

1. **Communities:** Add to relevant communities
   - Artificial Intelligence
   - Software Engineering
   - Open Science

2. **Keywords:** Add comprehensive tags
   - agentic-ai
   - rag-systems
   - ai-engineering
   - llmops
   - knowledge-management

3. **Related identifiers:** Link to:
   - Your ORCID
   - Related papers (when published)
   - Project website

4. **Funding:** Add grant information if applicable

## Using Your DOI

### In Papers
```latex
Our framework is openly available \cite{guan2025agenticai}.
Implementation details can be found at \url{https://doi.org/10.5281/zenodo.XXXXXXX}.
```

### In Presentations
"Framework DOI: 10.5281/zenodo.XXXXXXX"

### On Social Media
"Released Agentic-AI Framework v1.0! DOI: 10.5281/zenodo.XXXXXXX"

### In Grant Proposals
"We have established an open research framework (DOI: 10.5281/zenodo.XXXXXXX) that..."

## Monitoring Impact

Track your work's impact:
- **Zenodo Statistics:** View downloads and visits
- **Google Scholar:** Will index your DOI
- **Citations:** Track who cites your framework
- **GitHub Stars:** Community interest indicator

## Troubleshooting

**Q: Zenodo didn't capture my release**
- Ensure Zenodo integration is enabled
- Try manually syncing from Zenodo settings
- Check that the release is public, not draft

**Q: DOI isn't showing up**
- Wait a few minutes, processing can be delayed
- Check Zenodo uploads section
- Verify repository permissions

**Q: Want to update metadata after release**
- You can edit the Zenodo record directly
- Some fields are locked after publication
- Consider creating a new version for major changes

## Resources

- [Zenodo Documentation](https://help.zenodo.org/)
- [GitHub-Zenodo Integration Guide](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
- [Making Your Code Citable](https://guides.github.com/activities/citable-code/)
- [CITATION.cff Format](https://citation-file-format.github.io/)

---

**Next Steps:**
1. Create your GitHub release today
2. Obtain your DOI
3. Update CITATION.cff and README.md
4. Announce your framework with the DOI

This establishes permanent, citable precedence for your Agentic-AI Framework! 🎯

