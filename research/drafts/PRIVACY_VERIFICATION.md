# 🔒 Privacy Configuration Verification Guide

This guide helps you verify that your private drafts are **NOT** being tracked by Git and will never be pushed to GitHub.

---

## ✅ Quick Verification (30 seconds)

Run these commands to confirm everything is set up correctly:

### Windows (PowerShell)
```powershell
cd "D:\projects\Agentic-AI-Research-Roadmap"
git status
```

### macOS/Linux (Bash)
```bash
cd ~/projects/Agentic-AI-Research-Roadmap
git status
```

---

## 🎯 What You Should See

### ✅ **CORRECT Output**
```
On branch main
Changes not staged for commit:
  modified:   .gitignore
  modified:   README.md

Untracked files:
  drafts/README.md
  drafts/public/

no changes added to commit
```

**Key Points:**
- ✅ `drafts/private/` is **NOT** listed anywhere
- ✅ Files inside `private/` are **NOT** shown as "untracked"
- ✅ Only `drafts/public/` appears as untracked (before first commit)

---

### ❌ **INCORRECT Output (Fix Required)**
```
Untracked files:
  drafts/private/
  drafts/private/diva-workshop-paper.md
  drafts/private/USER_INPUT_NEEDED.md
```

**If you see this**, your `.gitignore` isn't working. Fix it:

```powershell
# Re-add the gitignore rule
echo "drafts/private/" | Out-File -Append -Encoding UTF8 .gitignore

# Remove any accidentally staged files
git rm --cached -r drafts/private/

# Verify
git status
```

---

## 🔍 Advanced Verification

### Test 1: Check .gitignore Rules
```powershell
git check-ignore -v drafts/private/diva-workshop-paper.md
```

**Expected Output:**
```
.gitignore:15:drafts/private/    drafts/private/diva-workshop-paper.md
```

This confirms the file is ignored by line 15 of `.gitignore`.

---

### Test 2: List Tracked Files in Drafts
```powershell
git ls-files drafts/
```

**Expected Output:**
```
drafts/README.md
drafts/public/.gitkeep
drafts/public/REVIEW_FEEDBACK_ACTION_PLAN.md
drafts/public/diva-publication-roadmap.md
drafts/public/workshop-paper-outline.md
```

**Should NOT include:**
- ❌ `drafts/private/diva-workshop-paper.md`
- ❌ `drafts/private/USER_INPUT_NEEDED.md`
- ❌ `drafts/private/README.md`

---

### Test 3: Simulate Push (Dry Run)
```powershell
# See what WOULD be pushed (without actually pushing)
git add -A
git status
```

**Verify:**
- ✅ No `drafts/private/` files are staged
- ✅ Only public files are ready to commit

**Important:** Run this before every push to GitHub!

---

## 🛡️ Safety Checklist Before Every Push

Before running `git push`, always verify:

- [ ] `git status` shows no `private/` files
- [ ] `git diff --cached` contains no sensitive data
- [ ] `.gitignore` includes `drafts/private/`
- [ ] Private files exist locally: `Test-Path drafts/private/diva-workshop-paper.md` returns `True`

---

## 🚨 Emergency: Private Files Were Pushed

If you accidentally pushed private files to GitHub:

### Step 1: Remove from Remote (Immediately!)
```powershell
# Remove files from Git history
git rm -r --cached drafts/private/
git commit -m "Remove private drafts from tracking"
git push origin main
```

### Step 2: Purge Git History (If Already Committed)
```powershell
# Install BFG Repo-Cleaner
# https://rtyley.github.io/bfg-repo-cleaner/

# Remove folder from all history
bfg --delete-folders private --no-blob-protection
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

⚠️ **Warning**: `git push --force` rewrites history. Coordinate with collaborators first!

### Step 3: Rotate Any Exposed Secrets
If private files contained:
- API keys → regenerate them
- Unpublished data → contact journal/conference editor
- Proprietary configs → assess IP exposure

---

## 📊 File Privacy Status Summary

| File | Privacy Level | Git Tracked? | On GitHub? |
|------|--------------|--------------|------------|
| `drafts/public/diva-publication-roadmap.md` | ✅ Public | Yes | Yes |
| `drafts/public/workshop-paper-outline.md` | ✅ Public | Yes | Yes |
| `drafts/public/REVIEW_FEEDBACK_ACTION_PLAN.md` | ✅ Public | Yes | Yes |
| `drafts/private/diva-workshop-paper.md` | 🔒 Private | **NO** | **NO** |
| `drafts/private/USER_INPUT_NEEDED.md` | 🔒 Private | **NO** | **NO** |

---

## 🔄 Backup Strategy for Private Files

Since private files aren't in Git, use these backup methods:

### Option 1: Encrypted Cloud Storage
```powershell
# OneDrive with restricted folder
Copy-Item -Recurse drafts/private/ "$env:OneDrive\Research\DIVA-Private-Backup-$(Get-Date -Format 'yyyy-MM-dd')"
```

### Option 2: Encrypted Archive
```powershell
# Create password-protected zip
Compress-Archive -Path drafts/private/ -DestinationPath "DIVA-Private-$(Get-Date -Format 'yyyy-MM-dd').zip"
# Store in secure location
```

### Option 3: Version Control (Separate Repo)
```powershell
# Create a PRIVATE GitHub repo
cd drafts/private
git init
git remote add origin https://github.com/YOUR_USERNAME/diva-private-drafts.git
git push -u origin main
```

**Important**: Ensure the backup repo is set to **Private** in GitHub settings!

---

## 📞 Questions or Issues?

If you're unsure whether your setup is correct:

1. Run all verification tests above
2. Check `git ls-files` output
3. Review `.gitignore` line 15: `drafts/private/`
4. Test with a dummy file:
   ```powershell
   New-Item drafts/private/test.txt -Value "This should not appear in git status"
   git status  # Should NOT show test.txt
   Remove-Item drafts/private/test.txt
   ```

---

**Last Verified**: November 10, 2025  
**Configuration Version**: 1.0

