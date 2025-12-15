---
id: 004
title: Create RAG Backend Implementation Tasks
stage: tasks
date: 2025-12-10
surface: agent
model: gemini-2.0-flash-exp
feature: rag-chatbot-backend
branch: main
user: Hamza
command: /sp.tasks
labels: ["tasks", "implementation", "rag", "backend"]
links:
  spec: specs/rag-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/rag-chatbot-backend/tasks.md
tests:
  - tests/test_rag.py
---

## Prompt

/sp.tasks

Break down RAG backend implementation into testable tasks.

**Scope:**

1. Setup project structure
2. Implement app/main.py
3. Implement app/rag.py
4. Create tests/test_rag.py
5. Create Dockerfile
6. Create README.md
7. Configure environment
8. Integration testing

## Response snapshot

# RAG Backend Implementation Tasks

## Task 1: Setup Project Structure ✅

- Create requirements.txt (11 packages)
- Create .env.example
- Create .gitignore
- Create app/**init**.py

## Task 2: Implement FastAPI App (app/main.py) ✅

**Files**: app/main.py (99 lines)
**Features**:

- FastAPI app with CORS
- Pydantic models (AskRequest, AskSelectionRequest, AskResponse)
- 4 endpoints (/, /api/health, /api/ask, /api/ask-selection)
- Error handling

**Test**: `curl http://localhost:8000/api/health`

## Task 3: Implement RAG Engine (app/rag.py) ✅

**Files**: app/rag.py (167 lines)
**Features**:

- RAGEngine class
- Gemini client (AsyncOpenAI)
- Qdrant client
- Methods: embed_query, search_vectors, build_prompt, generate_answer, ask, ask_selection

**Test**: `python -c "from app.rag import RAGEngine; print('OK')"`

## Task 4: Create Unit Tests (tests/test_rag.py) ✅

**Files**: tests/test_rag.py (85 lines)
**Tests**:

1. test_health_check
2. test_ask_endpoint
3. test_ask_selection_endpoint
4. test_ask_invalid_request
5. test_ask_selection_invalid_request

**Run**: `pytest tests/ -v`

## Task 5: Create Dockerfile ✅

**Features**:

- Python 3.10-slim
- Install requirements
- Expose port 7860
- Run uvicorn

**Test**: `docker build -t rag-backend .`

## Task 6: Create README.md ✅

**Features**:

- HF Spaces frontmatter
- API documentation
- Setup instructions
- Environment variables

## Task 7: Environment Configuration ✅

**Files**: .env, .env.example
**Variables**: GEMINI_API_KEY, QDRANT_URL, COLLECTION_NAME

## Task 8: Integration Testing ✅

**Files**: test_api.py, verification.py
**Tests**: All endpoints with real backend

## Summary

**Total**: 8 tasks ✅
**Files**: 3 core (main.py, rag.py, db.py) + tests + config
**Tests**: 5 unit tests + integration

## Outcome

- ✅ Impact: Complete task breakdown
- 🧪 Tests: 5 unit tests defined
- 📁 Files: tasks.md created
- 🔁 Next prompts: /sp.implement
- 🧠 Reflection: Clear, testable tasks

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): concise-tasks-v1
- Next experiment (smallest change to try): Implement backend
