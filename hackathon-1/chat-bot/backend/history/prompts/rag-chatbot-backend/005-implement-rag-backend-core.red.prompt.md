---
id: 005
title: Implement RAG Backend Core
stage: red
date: 2025-12-10
surface: agent
model: gemini-2.0-flash-exp
feature: rag-chatbot-backend
branch: main
user: Hamza
command: /sp.implement
labels: ["implementation", "backend", "rag", "fastapi"]
links:
  spec: specs/rag-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - app/main.py
  - app/rag.py
  - app/db.py
  - requirements.txt
  - Dockerfile
  - README.md
  - .env.example
tests:
  - tests/test_rag.py
---

## Prompt

/sp.implement

Implement the Physical AI Textbook RAG Backend with these core files:

1. **app/main.py** - FastAPI app with 4 endpoints (/, /api/health, /api/ask, /api/ask-selection)
2. **app/rag.py** - RAG engine with Gemini 2.5 Flash + Qdrant
3. **tests/test_rag.py** - 5 unit tests for endpoints
4. **requirements.txt** - 11 dependencies (fastapi, uvicorn, openai, qdrant-client, etc.)
5. **Dockerfile** - HF Spaces deployment config
6. **README.md** - API documentation with HF frontmatter

Key implementation details:

- Use AsyncOpenAI with Gemini compatibility endpoint
- Qdrant for vector storage (768 dim, cosine similarity)
- Top-3 retrieval, 200 token limit, temperature 0.5
- CORS for localhost:3000 and wildcard
- Mock RAGEngine in tests with AsyncMock

## Response snapshot

Implemented complete RAG backend with 3 core files:

**app/main.py** (99 lines):

- FastAPI app with CORS middleware
- Pydantic models: AskRequest, AskSelectionRequest, AskResponse
- 4 endpoints: /, /api/health, /api/ask, /api/ask-selection
- Error handling with try-catch and HTTPException

**app/rag.py** (167 lines):

- RAGEngine class with Gemini + Qdrant integration
- Methods: embed_query, search_vectors, build_prompt, generate_answer, ask, ask_selection, index_chunk
- text-embedding-004 for embeddings (768 dim)
- gemini-2.5-flash for generation (temp 0.5, max_tokens 200)
- Top-3 retrieval with 500 char limit per chunk

**tests/test_rag.py** (85 lines):

- 5 test cases: health check, ask endpoint, ask-selection, validation errors
- Mocked RAGEngine with AsyncMock
- FastAPI TestClient for endpoint testing

**Supporting files**:

- requirements.txt: 11 packages
- Dockerfile: Python 3.10-slim, port 7860
- README.md: HF Spaces frontmatter + API docs
- .env.example: GEMINI_API_KEY, QDRANT_URL, COLLECTION_NAME

All tests passing. Backend ready for deployment.

## Outcome

- ✅ Impact: Complete RAG backend with minimal 3-file architecture
- 🧪 Tests: 5 unit tests passing with mocked RAGEngine
- 📁 Files: Created 3 core files + tests + deployment config
- 🔁 Next prompts: /sp.implement for frontend integration
- 🧠 Reflection: Minimal implementation matches specification exactly

## Evaluation notes (flywheel)

- Failure modes observed: None - all tests passing
- Graders run and results (PASS/FAIL): PASS - 5/5 tests
- Prompt variant (if applicable): minimal-backend-v1
- Next experiment (smallest change to try): Integrate backend with Docusaurus frontend
