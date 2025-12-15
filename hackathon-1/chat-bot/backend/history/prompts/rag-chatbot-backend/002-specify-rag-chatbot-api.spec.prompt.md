---
id: 002
title: Specify RAG Chatbot Backend API
stage: spec
date: 2025-12-10
surface: agent
model: gemini-2.0-flash-exp
feature: rag-chatbot-backend
branch: main
user: Hamza
command: /sp.spec
labels: ["specification", "rag", "api-design", "gemini"]
links:
  spec: specs/rag-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/rag-chatbot-backend/spec.md
tests:
  - null
---

## Prompt

/sp.spec

Create detailed specification for Physical AI Textbook RAG Backend API.

**Define:**

1. API endpoints with request/response schemas
2. RAG pipeline (embedding → retrieval → generation)
3. Environment variables
4. CORS configuration
5. Error handling

## Response snapshot

# Physical AI RAG Backend Specification

## API Endpoints

### POST /api/ask

**Request**: `{"question": "string"}`
**Response**: `{"answer": "string", "sources": [{"chapter": "string", "score": number}]}`

### POST /api/ask-selection

**Request**: `{"question": "string", "selection": "string"}`
**Response**: `{"answer": "string"}`

### GET /api/health

**Response**: `{"status": "ok", "service": "physical-ai-textbook-api", "model": "gemini-1.5-flash"}`

### GET /

**Response**: `{"message": "...", "docs": "/docs", "health": "/api/health"}`

## RAG Pipeline

**Embedding**: text-embedding-004 (768 dim) via Gemini API
**Vector Store**: Qdrant with cosine similarity
**Retrieval**: Top-3 chunks, 500 chars each, score >0.0
**Generation**: gemini-2.5-flash, temp 0.5, max 200 tokens

**Prompt Template**:

```
You are a robotics tutor. Answer concisely in 2-3 sentences.
Context: [Chapter]: {text}
Q: {question}
A:
```

## Data Models

```python
class AskRequest(BaseModel):
    question: str

class AskSelectionRequest(BaseModel):
    question: str
    selection: str

class AskResponse(BaseModel):
    answer: str
    sources: List[dict] = []
```

## Environment Variables

```env
GEMINI_API_KEY=required
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=optional
COLLECTION_NAME=physical-ai-textbook
```

## CORS

- Origins: `["*", "http://localhost:3000"]`
- Methods: All
- Headers: All
- Credentials: True

## Error Handling

- 422: Validation error
- 500: Internal error with detail message
- Print errors + stack traces to console

## Outcome

- ✅ Impact: Complete API specification
- 🧪 Tests: Test criteria for each endpoint
- 📁 Files: spec.md created
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Clear contracts defined

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): concise-spec-v1
- Next experiment (smallest change to try): Create architecture plan
