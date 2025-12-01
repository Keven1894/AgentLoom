# 🚀 Privacy Protection - Quick Reference

> **TL;DR**: Files in `drafts/private/` will never be pushed to GitHub, automatically protected by `.gitignore`.

---

## 📂 File Locations

```
Local:  D:\projects\Agentic-AI-Research-Roadmap\drafts\private\
        ├── diva-workshop-paper.md      (full paper draft)
        └── USER_INPUT_NEEDED.md        (sensitive project data)

GitHub: ❌ These files do not exist (excluded by .gitignore)
```

---

## ⚡ Common Commands

### Verify Privacy Settings (5 seconds)
```powershell
git status  # Should NOT see private/ files
```

### Commit Public Content
```powershell
git add .gitignore README.md drafts/public/ drafts/*.md
git commit -m "docs: update public drafts"
git push
```

### Edit Private Files
```powershell
code drafts/private/diva-workshop-paper.md
# Save and done - automatically stays private
```

### Publish After Acceptance
```powershell
Move-Item drafts/private/paper.md drafts/public/
git add drafts/public/paper.md
git commit -m "docs: publish paper after acceptance"
git push
```

---

## 🔍 Pre-Push Checklist

- [ ] `git status` - confirm no private/ files shown
- [ ] `git diff --cached` - review staged changes
- [ ] Run `git ls-files drafts/ | Select-String "private"` - should return empty

---

## 📚 Full Documentation

| Need | See Document |
|------|--------------|
| 🔍 Verification steps | [PRIVACY_VERIFICATION.md](PRIVACY_VERIFICATION.md) |
| 📖 Complete policy | [README.md](README.md) |

---

## 🆘 Emergency

### Accidentally committed private files?
```powershell
git rm --cached drafts/private/file.md
git commit -m "Remove private file"
git push
```

### Configuration not working?
```powershell
# Verify .gitignore rule
git check-ignore -v drafts/private/diva-workshop-paper.md
# Should show: .gitignore:15:drafts/private/
```

---

## ✅ Security Guarantees

| Question | Answer |
|----------|--------|
| Will private files be pushed? | ❌ No |
| Can GitHub see them? | ❌ No |
| Manual operation needed? | ❌ No - automatic |
| Originality protected? | ✅ Yes - Git timestamps |

---

**Remember**: Private files exist only on your computer, GitHub cannot see them! 🔒

