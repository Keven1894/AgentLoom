# Skill Design - Creating Agent Capabilities

**Category**: Agent Design  
**Audience**: AI Agent Developers  
**Version**: 1.0

---

## What Are Skills?

**Skills** (Track 3) define **WHAT** an agent can DO:
- Concrete capabilities
- Executable actions
- Tool usage
- Procedures

Think of skills as the agent's "toolbox" of capabilities.

---

## Skill vs Behavior vs Knowledge

```
Behavior (Track 1):  HOW to teach students
Knowledge (Track 2): WHAT content to teach
Skill (Track 3):     WHAT ACTIONS to take (e.g., explain, guide, reference)
```

**Example**:
- **Behavior**: "Use pedagogical approach - guide don't tell"
- **Knowledge**: "Module 2: UML Class Diagrams"
- **Skill**: "explain-with-examples" - Take a concept and create explanation with examples

---

## Skill Structure

### Directory Layout
```
agents/skills/[role]/[category]/[skill-name]/
├── skill.md           # Specification (REQUIRED)
├── implementation/    # Code if needed (optional)
│   └── script.py
├── tests/            # Test cases (recommended)
│   └── test_skill.py
└── examples/         # Example usage (recommended)
    └── example.md
```

### skill.md Template
```markdown
---
id: "[role]-skill:[category]/[skill-name]"
name: "Human Readable Name"
category: "category-name"
role: "ta | developer | shared"
version: "1.0"
status: "active | planned | deprecated"
---

# Skill: [Name]

## Purpose
One sentence: What this skill does

## When to Use
- Scenario 1
- Scenario 2

## Inputs
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| param1    | str  | Yes      | Description |

## Outputs
| Return | Type | Description |
|--------|------|-------------|
| result | str  | Description |

## Dependencies
### Behaviors
- [Behavior Name](path/to/behavior.md)

### Knowledge
- [Knowledge Doc](path/to/doc.md)

### Other Skills
- [Other Skill](path/to/skill.md)

### Tools/Libraries
- Tool name (version)

## Logic
High-level algorithm or procedure:
1. Step 1
2. Step 2
3. Step 3

## Examples
### Example 1: [Scenario]
\`\`\`
Input: ...
Process: ...
Output: ...
\`\`\`

## Error Handling
- Error type 1: How to handle
- Error type 2: How to handle

## Testing
How to test this skill

## Notes
Additional information, caveats, limitations

## Related
- [Related Skill](path)
- [Related Behavior](path)
```

---

## Skill Categories

### For TA Role

**Teaching Skills**
- `answer-concepts` - Answer conceptual questions
- `explain-with-examples` - Explain using examples
- `guide-problem-solving` - Guide without giving answers

**Communication Skills**
- `reference-materials` - Cite course materials
- `check-understanding` - Verify comprehension
- `clarify-questions` - Handle ambiguous queries

**Assessment Skills**
- `study-guidance` - Provide study tips
- `exam-prep` - Help with exam preparation

### For Developer Role

**Analysis Skills**
- `analyze-course-materials` - Understand content structure
- `identify-structure` - Find organizational patterns
- `extract-metadata` - Pull out metadata

**Processing Skills**
- `process-pdf` - Extract text from PDFs
- `process-word` - Convert Word to markdown
- `process-html` - Convert HTML to markdown

**KG Management Skills** ⚡ CRITICAL
- `auto-integrate` - Auto-add content to KG
- `intelligent-linking` - Discover relationships
- `verify-integrity` - Validate KG connectivity
- `sync-filesystem` - Keep KG and files in sync

**Construction Skills**
- `create-knowledge-graph` - Build KG structures
- `write-documentation` - Create docs
- `build-skills` - Create skill definitions

**Validation Skills**
- `verify-connectivity` - Check KG connectivity
- `check-links` - Validate all links
- `validate-json` - Ensure JSON validity

---

## Design Principles

### 1. Single Responsibility
```
Each skill does ONE thing well
Don't create mega-skills
```

**Bad**:
```
skill: handle-student-query
- Parses question
- Checks integrity
- Searches knowledge
- Formats response
- Logs interaction
(Too much!)
```

**Good**:
```
skill: answer-concepts
- Takes parsed question
- Returns concept explanation
- Uses knowledge base
- Delegates formatting
```

### 2. Clear Interface
```
Inputs and outputs well-defined
No ambiguity about usage
```

```markdown
## Inputs
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| question  | str  | Yes      | The concept question |
| context   | dict | No       | Additional context |

## Outputs
| Return     | Type | Description |
|------------|------|-------------|
| answer     | str  | Explanation text |
| references | list | Course material refs |
```

### 3. Documented Dependencies
```
Explicit about what skill needs
Links to behaviors, knowledge, other skills
```

```markdown
## Dependencies
### Behaviors
- [Pedagogical Approach](...) - Guides explanation style

### Knowledge
- [Course Content](...) - Source of concepts

### Other Skills
- [reference-materials] - To cite sources
```

### 4. Error Handling
```
Graceful failure
Clear error messages
Fallback strategies
```

```markdown
## Error Handling
- **QuestionUnclear**: Ask clarifying questions
- **TopicNotFound**: Admit limitation, suggest alternatives
- **KnowledgeUnavailable**: Fallback to general principles
```

### 5. Testable
```
Include test cases
Provide examples
Enable validation
```

```markdown
## Testing
### Test Case 1: Valid Concept Question
Input: "What is the Adapter pattern?"
Expected: Explanation with example
Validates: Core functionality

### Test Case 2: Out of Scope
Input: "What is quantum computing?"
Expected: Polite redirect
Validates: Boundary handling
```

---

## Skill Types

### 1. LLM-Powered Skills
Use language model to generate responses.

**Characteristics**:
- Natural language input
- Contextual understanding
- Creative generation
- Requires prompt engineering

**Examples**:
- `answer-concepts` (TA)
- `explain-with-examples` (TA)
- `intelligent-linking` (Developer)

**Implementation**:
```python
def answer_concepts(question: str, context: dict) -> dict:
    """Use LLM to answer conceptual question"""
    prompt = build_prompt(question, context)
    response = llm.generate(prompt)
    references = extract_references(response)
    return {
        "answer": response,
        "references": references
    }
```

### 2. Rule-Based Skills
Follow explicit logic and rules.

**Characteristics**:
- Deterministic
- Fast execution
- Predictable
- No LLM needed

**Examples**:
- `verify-integrity` (Developer)
- `sync-filesystem` (Developer)
- `validate-json` (Developer)

**Implementation**:
```python
def verify_integrity(graph_path: str) -> dict:
    """Check KG connectivity"""
    graph = load_graph(graph_path)
    root = graph.root_node
    
    reachable = traverse_from_root(graph, root)
    all_nodes = set(graph.nodes.keys())
    orphaned = all_nodes - reachable
    
    return {
        "valid": len(orphaned) == 0,
        "orphaned_nodes": list(orphaned),
        "connectivity": len(reachable) / len(all_nodes)
    }
```

### 3. Hybrid Skills
Combine LLM intelligence with rule-based validation.

**Characteristics**:
- LLM for understanding/generation
- Rules for validation/safety
- Best of both worlds

**Examples**:
- `intelligent-linking` (Developer)
- `auto-integrate` (Developer)
- `guide-problem-solving` (TA)

**Implementation**:
```python
def intelligent_linking(node_id: str, graph: Graph) -> list:
    """Suggest links using LLM, validate with rules"""
    # LLM part: Understand content and suggest
    node_content = get_node_content(node_id)
    suggestions = llm.suggest_links(node_content, graph)
    
    # Rule part: Validate suggestions
    valid_links = []
    for link in suggestions:
        if validate_link(node_id, link, graph):
            valid_links.append(link)
    
    return valid_links
```

### 4. Tool-Wrapper Skills
Wrap external tools/libraries.

**Characteristics**:
- Standardizes tool usage
- Handles errors
- Provides consistent interface

**Examples**:
- `process-pdf` (Developer)
- `process-word` (Developer)
- `process-html` (Developer)

**Implementation**:
```python
def process_pdf(pdf_path: str) -> dict:
    """Extract text from PDF using external tool"""
    try:
        # Use external library
        text = pypdf.extract_text(pdf_path)
        metadata = pypdf.extract_metadata(pdf_path)
        
        # Clean and structure
        cleaned = clean_text(text)
        structured = identify_sections(cleaned)
        
        return {
            "success": True,
            "text": structured,
            "metadata": metadata
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
```

---

## Creating a New Skill

### Step-by-Step Process

**1. Identify Need**
```
What capability is missing?
What task needs automation?
What can't the agent currently do?
```

**2. Define Interface**
```markdown
Skill: process-pdf
Inputs: pdf_path (string)
Outputs: {text: string, metadata: dict}
```

**3. Document First**
```markdown
Create skill.md with:
- Purpose
- When to use
- Inputs/outputs
- Dependencies
- Logic outline
- Examples
```

**4. Choose Implementation Type**
```
LLM-powered? Rule-based? Hybrid? Tool-wrapper?
```

**5. Implement**
```python
Write the actual code or detailed procedure
```

**6. Test**
```python
Create test cases
Verify functionality
Test edge cases
```

**7. Integrate**
```
Add to knowledge graph
Link to relevant behaviors/knowledge
Update indexes
```

**8. Document Usage**
```markdown
Add examples
Document common issues
Provide troubleshooting
```

---

## Example: Creating `process-pdf` Skill

### 1. Identify Need
```
Need to extract text from PDF lecture notes
Current: Manual copy-paste (slow, error-prone)
Needed: Automated extraction
```

### 2. Define Interface
```markdown
Inputs:
  - pdf_path: Path to PDF file
  - options: {preserve_formatting: bool, extract_images: bool}

Outputs:
  - text: Extracted text content
  - images: List of extracted images (if requested)
  - metadata: {title, author, pages, created_date}
  - success: bool
  - errors: list of any errors
```

### 3. Document (skill.md)
```markdown
---
id: "dev-skill:processing/process-pdf"
name: "Process PDF"
category: "processing"
role: "developer"
version: "1.0"
status: "active"
---

# Skill: Process PDF

## Purpose
Extract text and metadata from PDF files for knowledge base integration.

## When to Use
- Processing course lecture PDFs
- Converting textbook chapters
- Extracting assignment descriptions

## Inputs
| Parameter           | Type | Required | Description |
|--------------------|------|----------|-------------|
| pdf_path           | str  | Yes      | Path to PDF |
| preserve_formatting| bool | No       | Keep layout |
| extract_images     | bool | No       | Extract images |

## Outputs
| Return   | Type | Description |
|----------|------|-------------|
| text     | str  | Extracted text |
| images   | list | Image files |
| metadata | dict | PDF metadata |

## Dependencies
### Tools/Libraries
- PyPDF2 (>=3.0) or pdfplumber

## Logic
1. Open PDF file
2. Extract text page by page
3. Clean and structure text
4. Extract metadata
5. Optionally extract images
6. Return structured results

## Examples
### Example 1: Basic Extraction
\`\`\`python
result = process_pdf("lecture-01.pdf")
if result["success"]:
    save_to_markdown(result["text"], "docs/ta/module-01/")
\`\`\`

## Error Handling
- **FileNotFound**: Return error, suggest checking path
- **CorruptedPDF**: Attempt repair, or fail gracefully
- **PermissionDenied**: Request proper permissions

## Testing
Test with:
- Simple text PDF
- Complex layout PDF
- Scanned PDF (OCR needed)
- Password-protected PDF
```

### 4-8. Implement, Test, Integrate
(See [Skill Creation Workflow](../../../.cursor/rules/workflows/developer/skill-creation.md))

---

## Common Pitfalls

### ❌ Don't

1. **Create God Skills**
   ```
   skill: do-everything
   NO - Too broad, unmaintainable
   ```

2. **Ignore Error Handling**
   ```
   Skill fails silently
   NO - Must handle and report errors
   ```

3. **Skip Documentation**
   ```
   "Code is self-documenting"
   NO - Document explicitly
   ```

4. **Forget Testing**
   ```
   "It works on my machine"
   NO - Test comprehensively
   ```

5. **Manual KG Updates**
   ```
   Create skill but don't add to graph
   NO - Always integrate with KG
   ```

### ✅ Do

1. **Single Responsibility**
2. **Document Everything**
3. **Test Thoroughly**
4. **Integrate with KG**
5. **Provide Examples**

---

## Related Documentation
- [3-Track Architecture](./3-track-architecture.md)
- [Knowledge Graphs](./knowledge-graphs.md)
- [Behavior Design](./behavior-design.md)

## Related Workflows
- [Skill Creation](../../../.cursor/rules/workflows/developer/skill-creation.md)
- [Testing & Validation](../../../.cursor/rules/workflows/developer/testing-validation.md)

---

**Last Updated**: November 18, 2025  
**Status**: Core documentation  
**Priority**: HIGH - Essential for building capabilities

