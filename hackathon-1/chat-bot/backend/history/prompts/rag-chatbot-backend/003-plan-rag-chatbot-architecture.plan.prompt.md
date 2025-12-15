---
id: 003
title: Plan RAG Chatbot Backend Architecture
stage: plan
date: 2025-12-10
surface: agent
model: gemini-2.0-flash-exp
feature: rag-chatbot-backend
branch: main
user: Hamza
command: /sp.plan
labels: ["architecture", "planning", "rag", "minimal-design"]
links:
  spec: specs/rag-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/rag-chatbot-backend/plan.md
tests:
  - null
---

## Prompt

/sp.plan

Create architectural plan for Physical AI RAG Backend based on actual minimal implementation.

**Actual Structure:**

```
backend/
├── app/
│   ├── main.py (99 lines) - FastAPI + endpoints
│   ├── rag.py (167 lines) - RAG engine
│   └── db.py (163 lines) - SQLite (not used for RAG)
├── tests/test_rag.py (85 lines)
├── requirements.txt, Dockerfile, README.md
```

**Key Decisions:**

1. Why 3-file structure?
2. Why Gemini via OpenAI SDK?
3. Why Qdrant over ChromaDB?
4. No rate limiting/auth?

## Response snapshot

# Physical AI RAG Backend Architecture Plan

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py (99 lines) - FastAPI app, CORS, endpoints
│   ├── rag.py (167 lines) - RAGEngine with Gemini + Qdrant
│   └── db.py (163 lines) - SQLite helpers (future use)
├── tests/
│   ├── __init__.py
│   └── test_rag.py (85 lines) - 5 unit tests
├── requirements.txt (11 packages)
├── Dockerfile (HF Spaces)
├── README.md
└── .env
```

## Component Architecture

### app/main.py

- FastAPI app with CORS middleware
- Pydantic models: AskRequest, AskSelectionRequest, AskResponse
- 4 endpoints: /, /api/health, /api/ask, /api/ask-selection
- Error handling with try-catch

### app/rag.py

- RAGEngine class
- Methods: embed_query, search_vectors, build_prompt, generate_answer, ask, ask_selection
- AsyncOpenAI client for Gemini
- Qdrant client for vectors

### tests/test_rag.py

- 5 tests: health, ask, ask-selection, validation errors
- Mock RAGEngine with AsyncMock
- FastAPI TestClient

## Data Flow

**RAG Pipeline**:

```
User → /api/ask → embed_query → search_vectors (top-3)
→ build_prompt → generate_answer → response
```

**Selection Pipeline**:

```
User → /api/ask-selection → build_prompt (no RAG)
→ generate_answer → response
```

## Key Design Decisions

### 1. Minimal 3-File Structure

**Why**: Simplicity, easy to understand, fast development
**Tradeoff**: Less modular, accepted for small project

### 2. Gemini via OpenAI SDK

**Why**: Familiar API, easy migration, official compatibility
**Tradeoff**: Extra dependency, accepted for convenience

### 3. Qdrant over ChromaDB

**Why**: Production-ready, cloud support, better API
**Tradeoff**: ChromaDB simpler, accepted for scalability

### 4. No Rate Limiting/Auth

**Why**: Zero bloat, HF Spaces handles infrastructure
**Tradeoff**: Potential abuse, accepted for MVP

## Deployment

**HF Spaces**: Docker SDK, port 7860
**Env Vars**: GEMINI_API_KEY, QDRANT_URL, COLLECTION_NAME
**Health Check**: /api/health endpoint

## Testing

**Unit Tests**: 5 tests with mocked RAGEngine
**Integration**: Manual testing with real APIs
**Coverage**: Focus on critical paths

## Outcome

- ✅ Impact: Minimal architecture plan matching real implementation
- 🧪 Tests: 5 test cases defined
- 📁 Files: plan.md created
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: 3-file architecture keeps it simple

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): minimal-plan-v1
- Next experiment (smallest change to try): Break down into tasks
