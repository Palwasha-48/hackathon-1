---
id: 001
title: Initialize RAG Chatbot Backend Constitution
stage: constitution
date: 2025-12-10
surface: agent
model: gemini-2.0-flash-exp
feature: rag-chatbot-backend
branch: main
user: Hamza
command: /sp.constitution
labels: ["constitution", "rag", "chatbot", "backend", "gemini"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

/sp.constitution

Create a constitution for the Physical AI Textbook RAG Chatbot Backend. This backend will provide intelligent Q&A capabilities for students learning about robotics, ROS2, Gazebo, Isaac Sim, and VLA systems.

**Core Requirements:**

1. Use Google Gemini 2.0 Flash for LLM reasoning (via OpenAI SDK compatibility)
2. Use Qdrant vector database for document retrieval
3. FastAPI for REST API endpoints
4. Support two modes: full RAG and selection-based Q&A
5. Deploy on Hugging Face Spaces
6. Integrate with Docusaurus frontend

**Key Principles:**

- Zero bloat: No authentication, user management, or unnecessary features
- Fast responses: Target <2s response time
- Accurate retrieval: Use Gemini's text-embedding-004 model
- Simple architecture: Minimal files, maximum clarity
- Production-ready: Proper error handling and CORS support

## Response snapshot

# Physical AI Textbook RAG Backend Constitution

## Project Principles

### 1. Simplicity First

- **Minimal Files**: Keep codebase small and focused (3-4 core files)
- **No Over-Engineering**: Avoid unnecessary abstractions and layers
- **Direct Implementation**: Straightforward code over clever patterns
- **Zero Bloat**: No authentication, user management, or legacy features
- **Single Purpose**: Pure knowledge serving API

### 2. Code Quality

- **Type Hints**: Use Python type hints for clarity
- **Docstrings**: Document all public functions
- **Error Handling**: Graceful failures with informative messages
- **Async/Await**: Use async for I/O operations
- **Clean Code**: Follow PEP 8 style guidelines

### 3. Architecture

- **FastAPI Core**: Modern, fast web framework
- **RAG Engine**: Centralized RAG logic in single module
- **Vector Store**: Qdrant for embeddings and retrieval
- **LLM Integration**: Gemini via OpenAI SDK compatibility layer
- **Stateless API**: No server-side session management

### 4. RAG Implementation

- **Embedding Model**: Google text-embedding-004 (768 dimensions)
- **LLM Model**: Gemini 2.0 Flash for generation
- **Retrieval**: Top-3 most relevant chunks
- **Context Window**: Limit to 500 chars per chunk
- **Prompt Engineering**: Concise 2-3 sentence responses

### 5. API Design

- **RESTful Endpoints**: Clear, intuitive API structure
  - `POST /api/ask` - Full RAG Q&A
  - `POST /api/ask-selection` - Explain selected text
  - `GET /api/health` - Health check
- **Pydantic Models**: Request/response validation
- **CORS**: Allow frontend domain access
- **Error Responses**: Proper HTTP status codes

### 6. Performance

- **Response Time**: Target <2s for 95th percentile
- **Concurrent Requests**: Support 10+ simultaneous users
- **Efficient Retrieval**: Limit context to top-3 chunks
- **Token Limits**: Max 200 tokens for responses
- **Temperature**: 0.5 for consistent answers

### 7. Deployment

- **Hugging Face Spaces**: Primary deployment target
- **Docker**: Containerized deployment
- **Port 7860**: HF Spaces default port
- **Environment Variables**: Secure API key management
- **Health Monitoring**: Health check endpoint

### 8. Testing

- **Unit Tests**: Test RAG endpoints
- **Integration Tests**: Test full API flow
- **Mock Testing**: Mock external API calls
- **Validation Tests**: Test request validation
- **Coverage**: Focus on critical paths

## Technology Stack

### Core Framework

- **FastAPI**: Modern async web framework
- **Uvicorn**: ASGI server

### RAG Components

- **Google Gemini 2.0 Flash**: LLM for generation
- **text-embedding-004**: Embedding model
- **Qdrant**: Vector database
- **OpenAI SDK**: Gemini compatibility layer

### Supporting Libraries

- **Pydantic**: Data validation
- **python-dotenv**: Environment management
- **httpx**: Async HTTP client
- **pytest**: Testing framework
- **pytest-asyncio**: Async test support

### Deployment

- **Hugging Face Spaces**: Hosting platform
- **Docker**: Containerization

## Success Criteria

1. ✅ Backend answers questions accurately about Physical AI topics
2. ✅ Response time <2 seconds for typical queries
3. ✅ Retrieval returns relevant context (top-3 chunks)
4. ✅ Selection-based Q&A works for highlighted text
5. ✅ Successfully deployed on Hugging Face Spaces
6. ✅ Frontend integration working without CORS issues
7. ✅ Tests passing for all endpoints
8. ✅ API documentation accessible at /docs

## Outcome

- ✅ Impact: Established foundational principles for minimal, focused RAG backend
- 🧪 Tests: Testing strategy defined with focus on critical paths
- 📁 Files: Created constitution.md with comprehensive guidelines
- 🔁 Next prompts: /sp.spec to define detailed API contracts
- 🧠 Reflection: Constitution emphasizes simplicity and zero bloat approach

## Evaluation notes (flywheel)

- Failure modes observed: None - constitution phase
- Graders run and results (PASS/FAIL): N/A - constitution phase
- Prompt variant (if applicable): minimal-architecture-v1
- Next experiment (smallest change to try): Proceed to specification with focus on actual implementation
