# Knowledge Graph Integrity

**Role**: Developer/Builder  
**Status**: ACTIVE  
**Priority**: CRITICAL  
**Version**: 1.0

---

## Purpose

Maintain 100% integrity and connectivity of all knowledge graphs at all times.

---

## Core Principle

> "A broken knowledge graph means a broken agent."

The knowledge graph is the foundation of the agent's self-awareness and capabilities.

---

## Integrity Requirements

### 1. Connectivity

- **100% connectivity**: Every node must be reachable from root
- **No orphans**: No nodes without incoming links (except root)
- **Valid links**: All links point to existing nodes

### 2. Structure

- **Valid JSON**: All graph files must be valid JSON
- **Required fields**: All nodes have id, type, path
- **Consistent IDs**: Node IDs follow naming conventions
- **Link types**: Use defined link type vocabulary

### 3. Synchronization

- **File system**: Graph nodes match actual files
- **Cross-track**: Track relationships are correct
- **Metadata**: Node metadata reflects file content

---

## Validation Checklist

Before committing any KG changes:

- [ ] All JSON files are valid
- [ ] All nodes reachable from root
- [ ] No orphaned nodes
- [ ] All links point to existing nodes
- [ ] No duplicate node IDs
- [ ] Cross-track links are bidirectional
- [ ] Metadata is current
- [ ] Visualization renders correctly

---

## Automatic Checks

### On Every KG Modification

```yaml
Triggers:
  - After adding node
  - After adding link
  - After deleting node
  - After updating metadata

Actions:
  - Run verify-integrity skill
  - Block commit if checks fail
  - Report issues clearly
  - Suggest fixes
```

### Scheduled Checks

```yaml
Daily:
  - Full graph validation
  - Sync with filesystem
  - Check for stale nodes

Weekly:
  - Deep integrity analysis
  - Cross-track validation
  - Pattern discovery
```

---

## Common Issues & Fixes

### Issue: Orphaned Node

**Cause**: Node created but not linked  
**Fix**: Add hierarchical link to parent or delete node

### Issue: Broken Link

**Cause**: Target node deleted but link remains  
**Fix**: Remove the link or restore target node

### Issue: Stale Node

**Cause**: File deleted but node remains  
**Fix**: Delete node and cascade link removal

### Issue: Missing Cross-Track Link

**Cause**: Behavior references skill but no link  
**Fix**: Add cross-track link in both graphs

---

## Recovery Procedures

### If Integrity Check Fails

1. **Don't commit**
2. **Review the errors**
3. **Fix the issues**
4. **Re-run validation**
5. **Only commit when passing**

### If Graph is Corrupted

1. **Restore from git backup**
2. **Identify what changed**
3. **Fix the root cause**
4. **Re-apply changes correctly**
5. **Validate thoroughly**

---

## Tools & Skills

### Validation Tools

- `shared/tools/kg-core/graph-validator.js`
- `shared/tools/kg-core/graph-query.js`

### Related Skills

- `dev-skill:kg-management/verify-integrity`
- `dev-skill:kg-management/sync-filesystem`
- `dev-skill:kg-management/validate-cross-track`

---

## Metrics to Track

- **Connectivity**: Always 100%
- **Orphan count**: Always 0
- **Broken links**: Always 0
- **Sync percentage**: Always 100%
- **Validation time**: < 2 seconds

---

## Related Behaviors

- [System Safety](../core/system-safety.md)
- [Validation Protocol](../core/behavior-validation.md)
- [KG-First Retrieval](../core/behavior-kg-first-retrieval.md)

---

**Last Updated**: November 30, 2025  
**Status**: Active - This is the foundation of self-evolution
