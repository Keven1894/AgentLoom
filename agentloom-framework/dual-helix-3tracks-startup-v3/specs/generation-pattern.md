# Specification-Based Generation Pattern

## The Problem with Templates

Templates (copy + replace placeholders) fail because:

1. LLMs are bad at precise find-and-replace
2. Placeholder syntax looks like valid content
3. Emoji encoding gets corrupted during copy
4. No validation that substitution was complete

## The Solution: Generate from Specification

Instead of copying templates, **generate fresh content** from specifications.

### Why This Works

LLMs excel at:

- Understanding requirements
- Generating coherent, consistent output
- Following structural rules
- Adapting to context

LLMs struggle with:

- Precise positional edits
- Character-level substitution
- Preserving encoding through transforms

---

## How to Use Specifications

### Step 1: Gather Context Variables

Before generating anything, collect all required variables:

```
PROJECT_NAME = "GIS Data Catalog Manager"
DOMAIN_ROLE_NAME = "Catalog Curator"  
DOMAIN_ROLE_ID = "catalog-curator"
DOMAIN_ID = "gis-catalog"
```

### Step 2: Read the Specification

Load the relevant `.spec.md` file. This tells you:

- What to generate (functional requirements)
- What format to use (structural requirements)
- What constraints apply (validation criteria)

### Step 3: Generate Fresh

Using the specification as your guide and the context variables as your data, **generate the entire file from scratch**.

Do NOT:

- Copy a template
- Search and replace placeholders
- Modify an existing file

DO:

- Read the spec
- Understand the requirements
- Generate complete, correct content
- Use the context variables naturally

### Step 4: Validate

Run validation to confirm the output meets the specification.

---

## Example: Generating visualization.html

### Bad Approach (Template)

```
1. Copy visualization.html.template
2. Find "[Project Name]" → Replace with "GIS Data Catalog Manager"
3. Find "[domain-role-id]" → Replace with "catalog-curator"
... (agent misses some, encoding breaks)
```

### Good Approach (Specification)

```
1. Read specs/visualization-html.spec.md
2. Note: PROJECT_NAME = "GIS Data Catalog Manager"
3. Note: DOMAIN_ROLE_ID = "catalog-curator"
4. Generate complete HTML following the spec:
   - Include vis-network from CDN
   - Create sidebar with project name as header
   - Create buttons for each graph type
   - Implement graph loading functions
   - Apply correct colors and shapes
   ... (agent generates coherent, correct code)
```

---

## Specification Types

### Type 1: Schema Specifications

Define the structure and rules for data formats.

- `knowledge-graph-schema.spec.md`
- Used for: All JSON graph files

### Type 2: Functional Specifications  

Define what a file should DO, not exactly how.

- `visualization-html.spec.md`
- Used for: Complex generated files

### Type 3: Standard Specifications

Define EXACT content for standardized components.

- `agent-builder-graphs.spec.md`
- Used for: Components that should be identical across projects

### Type 4: Structural Specifications

Define the sections and organization, not exact content.

- `behavior-file.spec.md`
- Used for: Files that follow a pattern but vary in content

---

## When to Use Each Approach

| Content Type | Approach | Why |
|--------------|----------|-----|
| Agent Builder graphs | Standard spec → Generate exact content | Always the same |
| Domain role graphs | Schema spec + context → Generate | Varies by project |
| Visualization HTML | Functional spec + context → Generate | Complex, needs coherence |
| Behavior files | Structural spec + content → Generate | Pattern with variation |
| Documentation | Requirements only → Generate | Agent excels at this |

---

## Validation Strategy

### For JSON Files

Run `validate_graphs.py` after generation:

- Checks valid JSON
- Checks root exists
- Checks all parents valid
- Checks no orphans

### For HTML Files

Open in browser and verify:

- No console errors
- All buttons work
- Graphs load correctly

### For Markdown Files

Check:

- Required sections present
- No placeholder text remaining
- Links are valid

---

## Migration from Templates

If you have existing templates, convert them to specifications:

### Template → Specification Conversion

1. **Identify the purpose**: What should this file DO?
2. **Extract requirements**: What must it contain?
3. **Define variables**: What changes per project?
4. **Write validation criteria**: How to verify correctness?
5. **Remove literal content**: Keep only the specification

### Example Conversion

**Template** (bad):

```html
<h2>🧠 [Project Name]</h2>
<button onclick="loadGraph('[domain-role-id]-knowledge')">📚 Knowledge</button>
```

**Specification** (good):

```markdown
## Sidebar Requirements
- Header showing PROJECT_NAME
- Button group for domain role with buttons:
  - Knowledge graph (loads {DOMAIN_ROLE_ID}-knowledge)
  - Skills graph (loads {DOMAIN_ROLE_ID}-skills)
  - Behaviors graph (loads {DOMAIN_ROLE_ID}-behaviors)
```

---

## Benefits

1. **Consistent Output**: Same spec → Same structure (but fresh generation)
2. **No Encoding Issues**: No copy = no corruption
3. **Agent Strength**: Leverages generation, not substitution
4. **Validation**: Clear criteria to verify correctness
5. **Non-Technical Friendly**: User provides context, agent generates correctly
