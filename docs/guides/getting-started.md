# Getting Started with Agentic-AI Framework

This guide will help you understand and apply the Agentic-AI Engineering Framework to your projects.

## Overview

The Agentic-AI Framework provides a systematic methodology for building production-grade AI agents that learn from experience and evolve over time.

## The Five-Stage Loop

### 1. Context Capture
**Goal:** Collect operational traces from agent interactions

**What to capture:**
- API calls and responses
- User interactions
- Task execution steps
- Decision points
- Environmental state

**How to implement:**
```python
# Example: Basic logging setup
import logging
import json
from datetime import datetime

class ContextLogger:
    def __init__(self, log_dir="context_logs"):
        self.log_dir = log_dir
        self.logger = logging.getLogger("agentic_context")
        
    def log_interaction(self, interaction_type, data):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": interaction_type,
            "data": data
        }
        # Log to structured format
        self.logger.info(json.dumps(log_entry))
```

### 2. Documentation
**Goal:** Transform implicit knowledge into explicit artifacts

**What to document:**
- Architecture decisions (ADRs)
- Daily work summaries
- Agent behavior policies
- Edge cases and solutions

**Template: Architecture Decision Record**
```markdown
# ADR-001: Choice of Vector Database

## Status
Accepted

## Context
We need to store and retrieve semantic embeddings for our RAG system.

## Decision
Use Chroma for vector storage due to its simplicity and Python integration.

## Consequences
- Positive: Easy to set up, good documentation
- Negative: May need to migrate if scaling requirements change
- Neutral: Single-language implementation
```

### 3. Indexing
**Goal:** Organize knowledge for efficient retrieval

**Hybrid Indexing Architecture:**
- **Vector DB:** For semantic similarity
- **SQL DB:** For exact matching and metadata

**Example: Setting up Chroma**
```python
import chromadb
from chromadb.config import Settings

# Initialize Chroma client
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

# Create collection
collection = client.create_collection(
    name="agent_memory",
    metadata={"description": "Agent operational memory"}
)

# Add documents
collection.add(
    documents=["Context about task execution..."],
    metadatas=[{"source": "task_log", "date": "2025-11-08"}],
    ids=["task_001"]
)
```

### 4. RAG (Retrieval-Augmented Generation)
**Goal:** Ground agent responses in accumulated knowledge

**Basic RAG Pipeline:**
```python
from openai import OpenAI

def rag_query(query, collection, client):
    # 1. Retrieve relevant context
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    
    # 2. Assemble context
    context = "\n".join(results['documents'][0])
    
    # 3. Generate response with context
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Use the provided context to answer questions."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
    )
    
    return response.choices[0].message.content
```

### 5. Fine-Tuning
**Goal:** Distill experience into specialized models

**When to fine-tune:**
- You have >1000 high-quality examples
- Consistent patterns in domain reasoning
- Need for reduced latency/cost

**Example: Preparing training data**
```python
# Format for OpenAI fine-tuning
training_examples = []

for interaction in successful_interactions:
    training_examples.append({
        "messages": [
            {"role": "system", "content": "You are a domain expert."},
            {"role": "user", "content": interaction['query']},
            {"role": "assistant", "content": interaction['response']}
        ]
    })

# Save as JSONL
with open('training_data.jsonl', 'w') as f:
    for example in training_examples:
        f.write(json.dumps(example) + '\n')
```

## Quick Start Checklist

### Week 1: Setup
- [ ] Set up logging for context capture
- [ ] Create documentation structure (decision_log/, daily/)
- [ ] Choose and initialize vector database
- [ ] Set up SQL database for metadata

### Week 2: Basic Pipeline
- [ ] Implement context capture in your application
- [ ] Write your first ADR
- [ ] Index initial knowledge base
- [ ] Build simple RAG query function

### Week 3: Integration
- [ ] Connect RAG to your agent
- [ ] Test retrieval quality
- [ ] Document edge cases
- [ ] Iterate on indexing strategy

### Week 4: Evaluation
- [ ] Measure retrieval precision
- [ ] Track agent success rate
- [ ] Gather user feedback
- [ ] Plan next improvements

## Best Practices

### Documentation
- **Be consistent:** Use templates for ADRs and daily logs
- **Be timely:** Document decisions when made, not weeks later
- **Be specific:** Include context, alternatives considered, and rationale
- **Be concise:** Focus on key decisions and insights

### Indexing
- **Tag everything:** Rich metadata enables better retrieval
- **Version your knowledge:** Track how understanding evolves
- **Test retrieval:** Regularly check if you're getting relevant results
- **Monitor performance:** Index size affects query speed

### RAG
- **Verify sources:** Always include citations
- **Balance context:** Too little is vague, too much is noisy
- **Handle failures:** What if no relevant context is found?
- **Iterate prompts:** Experiment with system messages

### Fine-Tuning
- **Start with RAG:** Fine-tuning is expensive and irreversible
- **Curate carefully:** Quality > quantity for training data
- **Evaluate rigorously:** Compare against base model
- **Document everything:** Record training parameters and results

## Common Patterns

### Pattern 1: Decision Documentation Loop
```
Agent makes decision → Log decision + context → 
Document in ADR → Index for future retrieval →
Use in RAG for similar situations
```

### Pattern 2: Error Learning Loop
```
Agent encounters error → Capture error context →
Document solution → Index error pattern →
Retrieve when similar error occurs
```

### Pattern 3: Knowledge Refinement Loop
```
Initial knowledge → Agent uses it → Identify gaps →
Document improvements → Re-index → Better future performance
```

## Troubleshooting

### "My retrieval returns irrelevant results"
- Check embedding model quality
- Review metadata tagging strategy
- Experiment with chunk sizes
- Add negative examples

### "My agent isn't learning"
- Verify context is being captured
- Check if documentation is actually happening
- Ensure indexing pipeline is working
- Test RAG retrieval independently

### "System is too slow"
- Profile vector DB performance
- Consider caching frequent queries
- Optimize chunk sizes
- Use async operations where possible

## Example Projects

### Minimal Example: Task Logger
See `examples/task-logger/` for a simple implementation that:
- Logs task execution steps
- Documents decisions
- Builds searchable memory
- Retrieves relevant past tasks

### Complete Example: Data Processing Agent
See `examples/data-processor/` for a full implementation with:
- Context capture from data pipelines
- ADR documentation
- Hybrid indexing (Chroma + PostgreSQL)
- RAG for data quality rules
- Fine-tuned model for classification

## Next Steps

1. **Read the full roadmap:** [Agentic-AI Research Roadmap](Agentic-AI-Research-Roadmap.md)
2. **Check the timeline:** [Research Timeline 2025-2027](Research-Timeline-2025-2027.md)
3. **Explore case studies:** (Coming soon after paper publications)
4. **Join the community:** GitHub Discussions

## Resources

### Tools
- **Vector Databases:** Chroma, Qdrant, Weaviate, Pinecone
- **RAG Frameworks:** LangChain, LlamaIndex, Haystack
- **Documentation:** MkDocs, Docusaurus, Sphinx
- **AI Assistants:** Claude, GPT-4, Cursor

### Further Reading
- "Retrieval-Augmented Generation for Large Language Models" (2023)
- "Agentic Retrieval-Augmented Generation: A Survey" (2025)
- "AI Agents vs. Agentic AI: A Conceptual Taxonomy" (2025)

## Questions?

- Open an issue on GitHub
- Start a discussion
- Email: bguan@fiu.edu

---

**Ready to build your first agentic system? Start with context capture and documentation!** 🚀

