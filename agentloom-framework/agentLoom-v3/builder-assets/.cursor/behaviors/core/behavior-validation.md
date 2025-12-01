# Developer Workflow: Testing & Validation

**Role**: Developer/Builder  
**Status**: ACTIVE  
**Version**: 2.0

---

## Purpose

Enforces a strict testing and validation protocol to ensure agent quality, integrity, and reliability before deployment.

## 🤖 Agent Protocol

**Trigger**: When user requests "validate", "test", "check integrity", or before committing complex changes.

**Actionable Steps**:

1. **Identify Scope**: Determine if the change affects a single Unit (Level 1), a Component (Level 2), or the System (Level 4).
2. **Retrieve Guide**: Consult `docs:builder:validation-guide` for specific testing procedures, code examples, and checklists.
3. **Execute Validation**: Run the selected tests as defined in the guide.
4. **Report**: Summarize results. If PASS -> Proceed. If FAIL -> Stop and Fix.

**Constraint**: DO NOT commit code or update KGs if validation fails (Severity: High).

## Related Resources

* [Validation Guide](../../docs/builder/validation-guide.md) (Detailed How-To)
* [System Safety](./system-safety.md)
* [Knowledge Graph Integrity](../builder/behavior-consistency.md)
