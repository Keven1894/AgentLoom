---
type: behavior
category: builder
id: behavior:builder:consistency
priority: critical
roles:
  - role-builder
---

# Graph Consistency Protocol

## Description
Mandates that the Knowledge Graph must accurately reflect the file system state.

## Rules
1. **Zero Latency**: Graph updates should happen immediately after file system changes.
2. **Truth is on Disk**: The file system is the source of truth; the graph is the map.
3. **No Orphans**: Every semantic file must have a graph node.
