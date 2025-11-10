# DIVA Technical Architecture - Detailed Analysis
**Extraction Date:** 2025-11-10  
**Category:** Technical Architecture & System Design

---

## System Architecture Overview

### Multi-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    External Users/Systems                    │
│            (Emails, Web Requests, SSH Access)               │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                 Presentation & Interface Layer               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Apache     │  │ AI Frontend  │  │    Email     │     │
│  │   HTTPD      │  │   (HTML)     │  │   Gateway    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                  AI Agent Orchestration Layer                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              DIVA (Cursor-based Agent)                │  │
│  │  - Claude Sonnet 4.5 / GPT-5 (Cloud)                 │  │
│  │  - Llama 3.1 3B/8B (Local via Ollama)                │  │
│  │  - .cursor/rules/ (Institutional Memory)             │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Autonomous Background Agents                  │  │
│  │  - Content Watcher (docs → HTML automation)          │  │
│  │  - n8n Workflow Engine (email automation)            │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                    Application Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Dataverse   │  │  AI Backend  │  │   Scripts    │     │
│  │  6.0 (Java)  │  │  (Node.js)   │  │   (Python)   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                   Infrastructure Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Payara 6   │  │  PostgreSQL  │  │  Solr 9.0    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## Core System Components

### 1. Dataverse Application Platform

**Base Technology:**
- **Platform:** Dataverse 6.0 (Harvard open-source)
- **Language:** Java 17 (OpenJDK)
- **Framework:** Jakarta EE (formerly Java EE)
- **Frontend:** JavaServer Faces (JSF) with PrimeFaces
- **Server:** Payara 6 application server
- **Package:** `edu.harvard.iq.dataverse`

**Key Directories:**
```
/data/dataverse/                              # Source code
├── src/main/java/edu/harvard/iq/dataverse/  # Java sources
├── src/main/resources/                       # Resources, configs
├── src/test/                                 # Tests
└── scripts/                                  # Utilities

/data/payara6/glassfish/domains/domain1/
└── applications/dataverse-6.0/               # Deployed WAR
    ├── WEB-INF/classes/                      # Compiled classes
    ├── WEB-INF/lib/                          # Dependencies
    └── [web resources]                       # XHTML, CSS, JS

/var/www/dataverse/                           # Static assets
```

**Key Subpackages:**
- **API:** RESTful API endpoints (JAX-RS)
- **Authorization:** Authentication and authorization
- **Data Access:** Database access layers (JPA)
- **Engine:** Command pattern implementation
- **Export:** Data export functionality
- **Harvest:** OAI-PMH harvesting
- **Ingest:** Data ingestion and processing
- **Search:** Solr integration
- **Settings:** Application configuration

**Deployment Flow:**
1. Source code → Maven build → WAR file
2. WAR → Payara deployment → Extracted application
3. Apache HTTPD → Reverse proxy → Payara
4. Shibboleth SP → SSO authentication

---

### 2. AI Agent Layer (DIVA)

**Primary Agent: DIVA**

**Platform:** Cursor IDE
- Multi-model AI support
- Full codebase indexing
- Rule-based behavior control
- Terminal integration
- Git integration

**AI Models Used:**

| Model | Purpose | When Used | Location |
|-------|---------|-----------|----------|
| **Claude Sonnet 4.5** | Complex reasoning, architecture | Primary for planning, design, complex logic | Cloud (Anthropic API) |
| **GPT-5** | Alternative perspectives | When different approach needed | Cloud (OpenAI API) |
| **Llama 3.1 8B** | Local processing, content generation | Content automation, sensitive data | Local (Ollama) |
| **Llama 3.2 3B** | Fast local processing | Document reading, quick queries | Local (Ollama) |
| **Llama 3.2 1B** | Ultra-fast processing | Simple tasks (note: has censorship) | Local (Ollama) |

**Configuration System (v2.0 Tiered):**

```
.cursor/
├── diva-identity.md              # Core identity (loaded always)
├── environment.md                # Environment context
├── README.md                     # Quick reference
└── rules/
    ├── INDEX.md                  # Rules index
    ├── README.md                 # Documentation
    ├── core/                     # Tier 0: Always loaded
    │   ├── identity.md           # Role, behavior (Priority: Highest)
    │   ├── language.md           # English-only (Priority: Critical)
    │   └── env-safety.md         # Safety rules (Priority: High)
    ├── standards/                # Tier 1: Context-based loading
    │   ├── coding.md             # General code quality
    │   ├── dataverse.md          # Dataverse-specific
    │   ├── java.md               # Java standards
    │   └── scripts.md            # Script conventions
    ├── workflows/                # Tier 1: Process rules
    │   ├── daily.md              # Daily procedures
    │   ├── planning.md           # Plan-first workflow
    │   ├── learning-journey.md   # Learning updates
    │   └── model-usage.md        # Model selection
    ├── actions/                  # Tier 1: Standard procedures
    │   ├── email.md              # Email functions
    │   ├── credential-access.md  # Credential handling
    │   └── document-reader.md    # Doc comprehension
    └── archive/                  # Tier 3: Historical rules
        └── *.mdc                 # Superseded rules
```

**Token Efficiency:**
- **Before (v1.0):** All rules loaded every session
- **After (v2.0):** Tiered loading
- **Reduction:** 87% token savings
- **Benefit:** Faster loading, focused context

**Institutional Memory Mechanism:**

```javascript
// Problem: New agent session = fresh start, no memory

// Solution: Rules as persistent memory
// File: .cursor/rules/actions/email.md

### 📧 Email Sending
**CRITICAL: Always use sendDivaEmail() - NEVER create ad-hoc scripts!**

import { sendDivaEmail } from './ai-backend/mail/diva_mailer.js';
await sendDivaEmail({ 
  to: 'user@fiu.edu', 
  subject: 'Test', 
  body: 'Message' 
});

// Result: Every new agent session knows standard procedures
```

---

### 3. AI Backend Services (Node.js)

**Location:** `/home/bguan/projs/dataverse/ai-backend/`

**Architecture:**

```
ai-backend/
├── server.js              # Main API server
├── index.js               # Entry point
├── ecosystem.config.js    # PM2 configuration
│
├── mail/                  # Email functionality
│   ├── diva_mailer.js     # Master email function ⭐
│   ├── sender.js          # Core sending with retry
│   ├── templates.js       # Email templates
│   └── templates/         # Markdown templates
│       ├── status_update.md
│       ├── feature_complete.md
│       ├── fix_notification.md
│       └── error_report.md
│
├── storage/               # Work request management
│   ├── request_manager.js # Request CRUD operations
│   └── work_requests/     # JSON storage
│       ├── pending/
│       ├── in_progress/
│       ├── completed/
│       └── failed/
│
├── api/                   # API endpoints
│   └── auth.js            # Authentication
│
└── config/                # Configuration
    ├── email_config.js    # Email settings
    ├── paths.js           # Path configuration
    ├── authorized_users.json
    └── dataverse_core_team.json
```

**Master Email Function Design:**

```javascript
// diva_mailer.js - Centralized email sending
// Prevents ad-hoc email script creation

import nodemailer from 'nodemailer';
import { getEmailConfig } from '../config/email_config.js';

export async function sendDivaEmail({
  to,
  subject,
  body,
  html = null,
  attachments = []
}) {
  // Features:
  // - Automatic retry (3 attempts)
  // - Comprehensive logging
  // - Error handling
  // - Template support
  // - HTML formatting
  
  // Result: Standardized across all operations
}
```

**Email System Features:**
- ✅ Retry logic (3 attempts, exponential backoff)
- ✅ Template system (5 templates)
- ✅ HTML formatting
- ✅ Attachment support
- ✅ Comprehensive logging
- ✅ Error tracking
- ✅ 100% success rate in testing

**Storage System:**
```javascript
// Request lifecycle management
// JSON-based storage with state transitions

work_requests/
├── pending/         # New requests from n8n
├── in_progress/     # Currently being worked
├── completed/       # Successfully finished
└── failed/          # Errored or rejected

// Example request structure:
{
  "id": "uuid",
  "intent": "REQUEST | INQUIRY | DISCUSSION",
  "email": "sender@example.com",
  "subject": "Email subject",
  "body": "Email content",
  "workPlan": { ... },
  "status": "pending",
  "createdAt": "ISO timestamp",
  "processedAt": null,
  "result": null
}
```

---

### 4. Autonomous Agent: Content Watcher

**Purpose:** Automate HTML generation from markdown documentation

**Location:** `/home/bguan/projs/dataverse/agents/content-watcher/`

**Architecture:**

```
agents/content-watcher/
├── index.js                    # Main orchestrator
├── package.json                # Dependencies (97 packages)
│
├── config/
│   ├── content-mapping.json    # Maps docs → HTML sections
│   └── settings.js             # Configuration
│
├── lib/                        # Core components
│   ├── file-watcher.js         # Monitors docs/ with chokidar
│   ├── change-analyzer.js      # Determines affected sections
│   ├── content-aggregator.js   # Gathers multi-doc content
│   ├── llm-adapter.js          # Calls Llama 3.1 8B
│   ├── html-updater.js         # Updates HTML files
│   ├── git-handler.js          # Git automation
│   └── notifier.js             # Logging & email
│
└── prompts/                    # LLM prompts (section-specific)
    ├── system-prompt.txt       # Global instructions
    ├── quick-stats.txt         # Statistics generation
    ├── innovations.txt         # Innovation cards
    ├── timeline.txt            # Timeline entries
    └── skills-matrix.txt       # Skills grid
```

**Operational Flow:**

```
1. File watcher detects change in docs/
   ↓
2. Debounce (5 seconds - batch multiple edits)
   ↓
3. Change analyzer: "Which HTML sections are affected?"
   ↓
4. For each affected section:
   a. Content aggregator: Gather ALL related docs
   b. LLM adapter: Generate new HTML
   c. HTML updater: Replace section
   ↓
5. Git handler: Commit with message
   ↓
6. Notifier: Email summary
```

**Content Mapping Example:**

```json
{
  "index.html": {
    "quick-stats": {
      "selector": ".stats-badges",
      "sources": [
        "docs/diva/learning-journey/timeline.md",
        "docs/diva/learning-journey/skills-matrix.md",
        "docs/plan/worklog/*-SUMMARY.md"
      ],
      "prompt": "prompts/quick-stats.txt"
    }
  }
}
```

**Key Innovation: Multi-Source Aggregation**
- Not 1:1 mapping
- One section pulls from multiple docs
- LLM synthesizes content from all sources
- Ensures consistency across related information

**Performance:**
- Processing time: 30-60 seconds per section
- Full update: 5-10 minutes (7 sections)
- Model: Llama 3.1 8B (quality/speed balance)
- Reliability: 100% (no errors in testing)

**Automation Result:**
- Before: 30-60 minutes manual HTML editing
- After: 2-5 minutes automated
- Consistency: 100% (LLM follows templates)
- Human effort: Zero (edit markdown, walk away)

---

### 5. Email Automation: n8n Workflow Engine

**Purpose:** Receive and process emails autonomously

**Location:** Docker container on local machine

**Access:** http://localhost:5678

**Architecture:**

```
External Email → Gmail API → n8n Workflow → Shared Storage → DIVA Backend
                                    ↓
                         Email Acknowledgment
```

**Workflow Design:**

```
┌─────────────────────────────────────────┐
│  1. Gmail Trigger (poll every 5 min)   │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  2. Extract Email Data                  │
│     - From, Subject, Body               │
│     - Attachments                       │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  3. Intent Analyzer (Classification)    │
│     - REQUEST: "Can you help with..."   │
│     - INQUIRY: "What is...?"            │
│     - DISCUSSION: "I think..."          │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  4. Switch (Route by Intent)            │
├─────────────┬───────────────────────────┤
│  REQUEST    │  INQUIRY  │  DISCUSSION   │
└─────────────┼───────────┼───────────────┘
              ↓           ↓               ↓
    ┌─────────────┐ ┌─────────┐ ┌─────────────┐
    │  Generate   │ │  Flag   │ │    Flag     │
    │  Work Plan  │ │  for    │ │    for      │
    │             │ │ Research│ │   Review    │
    └─────────────┘ └─────────┘ └─────────────┘
              ↓
┌─────────────────────────────────────────┐
│  5. Store to Shared Storage             │
│     ai-backend/storage/work_requests/   │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  6. Send Acknowledgment Email           │
│     "Thank you, working on it..."       │
└─────────────┬───────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  7. Mark Email as Read                  │
└─────────────────────────────────────────┘
```

**Intent Classification Algorithm:**

```javascript
// Pattern-based classification (85%+ accuracy target)

const intents = {
  REQUEST: [
    /can you (help|assist|do)/i,
    /please (fix|update|add|create)/i,
    /need (you to|help with)/i,
    /could you/i
  ],
  INQUIRY: [
    /what (is|are|does|do)/i,
    /how (do|does|can)/i,
    /explain/i,
    /tell me about/i
  ],
  DISCUSSION: [
    /I think/i,
    /suggestion/i,
    /idea/i,
    /feedback/i
  ]
};

// Future: LLM-powered classification for better accuracy
```

**OAuth Configuration:**
- Gmail API scope: `gmail.readonly`, `gmail.modify`, `gmail.send`
- OAuth 2.0 (not app password)
- Credentials stored encrypted in n8n
- Test users: ai.agents.mailer@gmail.com

**Status (Nov 2025):**
- ✅ n8n installed and running
- ✅ Documentation complete
- ✅ Workflow designed
- 🔄 OAuth configuration (manual setup)
- 🔄 Awaiting IT port opening (587, 993)

---

### 6. Local LLM Integration

**Purpose:** Privacy-preserving, offline AI capabilities

**Platform:** Ollama (local LLM server)

**Models Deployed:**

| Model | Size | Use Case | Performance |
|-------|------|----------|-------------|
| Llama 3.1 8B | 2.0GB | Content generation, complex tasks | 3.6s avg, 52.6% accuracy |
| Llama 3.2 3B | 1.3GB | Document reading, faster processing | 3.1s avg, 52.6% accuracy |
| Llama 3.2 1B | 700MB | Ultra-fast queries | 2.5s avg, 35.8% accuracy (censored) |

**Research Findings (Document Comprehension):**

**Test Setup:**
- Document: .env file (54 lines, 1496 chars)
- Questions: 95 across 5 categories
- Difficulty: 30 easy, 43 medium, 22 hard

**Results:**

| Metric | Llama 3.2 1B | Llama 3.2 3B | Winner |
|--------|--------------|--------------|---------|
| Overall Accuracy | 35.8% | **52.6%** | 3B (+47%) |
| Explicit Credentials | 60.0% | **100%** | 3B (+40%) |
| Implicit Relationships | 42.3% | **65.4%** | 3B (+23%) |
| Ambiguous Terms | 26.3% | 26.3% | Tie |
| Multi-hop Reasoning | 20.0% | 20.0% | Tie |
| Structural Understanding | 20.0% | **40.0%** | 3B (+20%) |
| Avg Response Time | 3.10s | 3.61s | 1B (+16% faster) |
| Success Rate | 100% | 100% | Tie |

**Key Discovery: Model Censorship**
- Llama 3.2 1B has built-in censorship
- Refuses to provide credentials/passwords
- Example: "I can't provide information on this topic"
- Impact: 40% accuracy loss on credential questions
- **Lesson:** Model selection must consider behavioral characteristics, not just size

**Novel Technique: Schema-as-Chunking**

```json
// Treating document schemas like vector DB chunking

{
  "environments": {
    "dev": { "database": "localhost", "port": 5432 },
    "prod": { "database": "localhost", "port": 5432 }
  },
  "relationships": {
    "dev uses localhost": true,
    "prod uses localhost": true
  },
  "criticalFacts": [
    "⚠️ Both dev and prod use localhost",
    "⚠️ Production database is NOT dpantherdb04temp"
  ],
  "tips": [
    "localhost means local PostgreSQL instance",
    "dpantherdb04temp is mentioned but not used"
  ]
}
```

**Impact:**
- Without critical facts: 42.3% accuracy on implicit relationships
- With critical facts: 65.4% accuracy
- **+23% improvement from schema design**

**Production Use Cases:**
- ✅ Document reader tool (`ask_doc.py`)
- ✅ Content generation (Content Watcher Agent)
- ✅ Interactive troubleshooting
- ✅ Configuration exploration
- ⚠️ Automated scripts (requires validation)

**Architecture Benefits:**
- Privacy: No data leaves local machine
- Cost: Free after initial setup
- Latency: 3-4 seconds (acceptable)
- Reliability: 100% success rate
- Offline: Works without internet

---

### 7. Authentication & Security

**SSO Integration:**

```
User → Shibboleth SP → FIU Identity Provider → SAML Response → Dataverse
```

- **Provider:** FIU Shibboleth Sign-On
- **Protocol:** SAML 2.0
- **Configuration:** `/etc/shibboleth/shibboleth2.xml`
- **Metadata:** `dataverse-idp-metadata.xml`

**Credential Management:**

**Environment Manager (`env_manager.sh`):**
```bash
# Secure credential storage with automatic backups

./scripts/dev_tools/env_manager.sh set DB_PASSWORD "secret"
# Creates: .secure_store (encrypted)
# Backup: .secure_store.backup.1 ... .backup.10

./scripts/dev_tools/env_manager.sh get DB_PASSWORD
# Returns: secret

./scripts/dev_tools/env_manager.sh list
# Shows: DB_PASSWORD = ******* (masked)
```

**Features:**
- Automatic backups (last 10)
- Sensitive value masking
- LLM-friendly interface
- Git-ignored storage
- Backup rotation

**API Authentication (AI Backend):**
```javascript
// Whitelist-based authentication
// File: config/authorized_users.json

{
  "authorized_users": [
    "bguan@fiu.edu",
    "ai.agents.mailer@gmail.com"
  ]
}

// Simple but effective for internal use
```

---

### 8. Deployment & Operations

**Local CI/CD Architecture:**

```
Developer Machine (DIVA)
    ↓
SSH with credentials from .env
    ↓
Production Server (dataversedev.fiu.edu)
    ↓
Execute deployment scripts
    ↓
Verify and notify
```

**Deployment Tools:**

| Tool | Purpose | Usage |
|------|---------|-------|
| `dep-tools` | Universal file deployer | Copy any file to remote location |
| `rem-tools` | Remote command executor | Execute commands with sudo support |
| `app-deploy` | Dataverse WAR deployer | Deploy new application version |
| `doc-deploy` | Documentation deployer | Update public HTML docs |

**Example Deployment:**

```bash
# Deploy documentation (used by DIVA)
./scripts/deployment/doc-deploy

# Steps:
# 1. Upload HTML to /var/www/dataverse/ai/
# 2. Set permissions (web server user)
# 3. Configure Apache
# 4. Verify HTTP 200
# 5. Log operation

# Time: < 1 minute
# Result: Live at https://dataversedev.fiu.edu/ai/
```

**Advantages of Local CI/CD:**
- ⚡ Instant execution (no queue)
- 🔐 Credentials in local secure store
- 💰 Zero external service costs
- 🎯 Full visibility of operations
- 🛠️ Easy to add new deployment types

**Process Manager (PM2):**

```bash
# Run Node.js services as daemons

pm2 start ai-backend/server.js --name diva-backend
pm2 start agents/content-watcher/index.js --name diva-content-watcher

# Features:
# - Auto-restart on crash
# - Log management
# - Resource monitoring
# - Startup scripts
# - Process clustering
```

---

## Data Flow Patterns

### 1. Email Receipt & Processing

```
External User sends email
    ↓
Gmail: ai.agents.mailer@gmail.com
    ↓
n8n polls (every 5 min)
    ↓
Intent Analyzer classifies email
    ↓
Work Plan Generator (if REQUEST)
    ↓
JSON stored: ai-backend/storage/work_requests/pending/
    ↓
DIVA Backend polls storage
    ↓
Execute work plan
    ↓
Update status: in_progress → completed
    ↓
Send result email via diva_mailer.js
```

### 2. Documentation Update Flow

```
Human edits: docs/diva/learning-journey/timeline.md
    ↓
Content Watcher detects change (chokidar)
    ↓
Debounce 5 seconds
    ↓
Analyze: Affects index.html (quick-stats), diva-learning-journey.html (timeline)
    ↓
For each affected section:
  - Aggregate all related docs
  - Build context for LLM
  - Call Llama 3.1 8B via Ollama
  - Generate new HTML
  - Replace section in HTML file
    ↓
Git add + commit "Auto-update frontend content"
    ↓
Email summary to bguan@fiu.edu
```

### 3. Deployment Flow

```
Human: "Deploy the vibe coding guide"
    ↓
DIVA (Cursor agent):
  1. Read: ai-frontend/pages/meet-diva.html
  2. Execute: ./scripts/deployment/doc-deploy
  3. SSH to dataversedev.fiu.edu
  4. Upload to /var/www/dataverse/ai/
  5. Set permissions: chown apache:apache
  6. Verify: curl -I https://dataversedev.fiu.edu/ai/meet-diva.html
  7. Log operation
  8. Respond: "Deployed successfully"
    ↓
Result: Live in < 1 minute
```

### 4. Document Comprehension Flow

```
Human: "What is the production database password?"
    ↓
DIVA uses: ./scripts/dev_tools/ask_doc.py .env
    ↓
Script:
  1. Read .env file
  2. Load schema (structure, relationships, critical facts)
  3. Build context-rich prompt
  4. Call Llama 3.2 3B via Ollama
  5. Parse response
  6. Return with explanation
    ↓
Response: "localhost (Production uses local PostgreSQL, not remote server)"
```

---

## Integration Points

### External Systems

**1. FIU Identity Provider**
- Shibboleth SAML 2.0
- Federated authentication
- Attribute exchange

**2. Gmail API**
- OAuth 2.0 authentication
- Email sending/receiving
- Label management

**3. Ollama**
- Local LLM server (http://localhost:11434)
- Model management
- Inference API

**4. Git**
- Version control
- Automated commits
- History preservation

### Internal Integrations

**1. Cursor ↔ System**
- Terminal access
- File system operations
- Git operations
- SSH execution

**2. n8n ↔ AI Backend**
- Shared JSON storage
- File-based queue
- State management

**3. Content Watcher ↔ Git**
- Automated commits
- Commit message generation
- Push automation (optional)

**4. DIVA ↔ Ollama**
- Direct API calls
- Model selection
- Response streaming

---

## Performance Characteristics

### Response Times

| Operation | Time | Notes |
|-----------|------|-------|
| Email send | 2-5 seconds | Via Gmail API |
| LLM query (3B) | 3-4 seconds | Local Ollama |
| LLM query (8B) | 5-10 seconds | More complex |
| Content section update | 30-60 seconds | Includes LLM + HTML |
| Full content update | 5-10 minutes | 7 sections |
| File deployment | < 1 minute | SSH + verify |
| Documentation search | < 1 second | Grep-based |

### Resource Usage

| Service | Memory | CPU | Disk |
|---------|--------|-----|------|
| Payara 6 | 2-4GB | 10-20% | ~5GB |
| PostgreSQL | 500MB-1GB | 5-10% | ~10GB |
| Ollama (idle) | 200MB | 0% | ~10GB (models) |
| Ollama (3B inference) | 4GB | 80-100% | - |
| n8n | 200-300MB | 1-2% | ~50MB |
| Content Watcher | 100-200MB | 1-5% | - |
| AI Backend | 50-100MB | 0-2% | - |

### Scalability

**Current Capacity:**
- Email processing: ~100/day (5 min polling)
- Documentation updates: Unlimited (event-driven)
- Concurrent LLM requests: 1 (single Ollama instance)
- User load: Development team (5-10 users)

**Scaling Strategies:**
- Email: Reduce polling interval, add workers
- Content: Multiple watcher instances, model sharding
- LLM: GPU acceleration, model quantization, distributed Ollama
- Users: Load balancer, application clustering

---

## Reliability & Resilience

### Error Handling

**Email System:**
- Retry logic: 3 attempts with exponential backoff
- Fallback: Log error, notify admin
- Recovery: Automatic retry on next poll

**Content Watcher:**
- Debouncing: Batch rapid changes
- Backup: Original HTML preserved before update
- Validation: HTML syntax check before commit
- Rollback: Git revert if validation fails

**LLM Calls:**
- Timeout: 60 seconds max
- Fallback: Error message to user
- Retry: Automatic on connection errors
- Alternative: Switch to cloud model if local fails

### Monitoring

**Application:**
- Payara logs: `/data/payara6/.../logs/`
- Error tracking: Daily log review
- Health checks: HTTP endpoints

**AI Services:**
- PM2 monitoring: Resource usage, restart count
- Email logs: `ai-backend/logs/email-*.log`
- Content updates: Git commit history
- n8n logs: `docker logs n8n`

**System:**
- Disk usage: Alert at 80%
- Memory: Alert at 90%
- CPU: Alert at sustained 80%+

### Backup Strategy

**Configuration:**
- Credentials: 10 backups via env_manager
- Cursor rules: Git versioned
- n8n workflows: SQLite database backup
- Application configs: Daily backups

**Data:**
- PostgreSQL: Daily dumps
- Solr indices: Weekly snapshots
- Documentation: Git history
- Work requests: JSON files (persistent)

**Code:**
- Git commits: Multiple remotes
- Deployment scripts: Versioned
- Agent code: Git + backups

---

## Security Architecture

### Defense in Depth

**Layer 1: Network**
- Firewall: FIU network protection
- SSH: Key-based authentication only
- HTTPS: All external traffic
- VPN: Admin access required

**Layer 2: Application**
- Shibboleth: SSO authentication
- Permission checks: Role-based access
- Input validation: All user inputs
- SQL injection: Parameterized queries

**Layer 3: Data**
- Encryption at rest: Database encryption
- Encryption in transit: TLS 1.2+
- Credential storage: Encrypted .secure_store
- API keys: Environment variables only

**Layer 4: Operations**
- Principle of least privilege
- Audit logging: All operations
- Automated backups
- Regular security reviews

### Sensitive Data Handling

**DIVA Agent Rules:**
- Never commit credentials to Git
- Mask sensitive values in logs
- Use secure_store for secrets
- No credentials in error messages
- LLM-friendly but security-conscious

**Example Safe Pattern:**
```bash
# Environment manager masks sensitive values
$ ./scripts/dev_tools/env_manager.sh list
DB_PASSWORD=*******
API_KEY=*******
EMAIL_PASSWORD=*******

# But retrieval is explicit
$ ./scripts/dev_tools/env_manager.sh get DB_PASSWORD
my_secure_password_123
```

---

## Technology Dependencies

### Core Dependencies

**Java/Jakarta EE:**
- Java 17 (OpenJDK)
- Jakarta EE 9+ APIs
- Maven (build tool)
- JUnit (testing)

**JavaScript/Node.js:**
- Node.js 18+
- Express.js (API framework)
- nodemailer (email)
- chokidar (file watching)
- PM2 (process management)

**Python:**
- Python 3.8+
- requests (HTTP client)
- json (data handling)
- subprocess (command execution)

**Infrastructure:**
- Docker (n8n container)
- Ollama (local LLM server)
- Git (version control)
- SSH (remote access)

### AI Model Dependencies

**Cloud Models:**
- Anthropic Claude API
- OpenAI GPT API
- Internet connectivity required
- API keys managed securely

**Local Models:**
- Ollama installation
- Model files (2-10GB each)
- Sufficient RAM (4-8GB per model)
- CPU inference (or GPU optional)

---

## Architecture Evolution

### Version History

**Phase 1 (Initial):**
- Manual Dataverse management
- No AI assistance
- Ad-hoc scripting

**Phase 2 (DIVA Introduction):**
- Cursor-based agent
- Basic .cursor rules
- Manual email handling
- Documentation generation

**Phase 3 (Automation):**
- Master email function
- n8n integration (designed)
- Content Watcher agent
- Institutional memory system

**Phase 4 (Current):**
- Multi-model orchestration
- Local LLM integration
- Tiered configuration (v2.0)
- Research program active

**Phase 5 (Planned):**
- Multi-agent architecture
- Database-backed knowledge
- Semantic search (pgvector)
- MCP server integration

### Future Architecture Vision

```
┌─────────────────────────────────────────────────────────┐
│         Leader Agent (DIVA Orchestrator)                │
│  - Task planning and delegation                         │
│  - Multi-agent coordination                             │
│  - Context management                                   │
└────────────────────┬────────────────────────────────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
    ▼                ▼                ▼
┌─────────┐    ┌─────────┐    ┌─────────┐
│  Admin  │    │   Dev   │    │ Content │
│  Agent  │    │  Agent  │    │  Agent  │
└─────────┘    └─────────┘    └─────────┘
    │                │                │
    └────────────────┼────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   Knowledge Base      │
         │  (PostgreSQL+pgvector)│
         └───────────────────────┘
```

---

## Summary: Architectural Strengths

**1. Multi-Layer Resilience**
- Cloud + local AI models
- Multiple deployment strategies
- Comprehensive error handling
- Extensive backups

**2. Privacy-First Design**
- Local LLM capabilities
- Secure credential management
- No unnecessary cloud dependencies
- Data sovereignty maintained

**3. Automation-Friendly**
- Git integration throughout
- PM2 process management
- Webhook-ready architecture
- Extensible agent system

**4. Production-Ready**
- Real operational deployment
- Comprehensive monitoring
- Security in depth
- Scalability planned

**5. Research-Validated**
- Local LLM performance measured
- Institutional memory proven
- Content automation validated
- Multi-model orchestration working

---

**Document Status:** Complete technical architecture extraction  
**Next:** Agent Design Patterns (02-AGENT-DESIGN-PATTERNS.md)

