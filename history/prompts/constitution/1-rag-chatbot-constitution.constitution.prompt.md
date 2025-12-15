---
id: 1
title: RAG Chatbot Constitution
stage: constitution
date: 2025-12-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-book-content
user: Wajiz.pk
command: /sp.constitution
labels: ["constitution", "rag", "chatbot", "physical-ai"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Integrated RAG Chatbot Development:
i want to Build and embed a Retrieval-Augmented Generation (RAG) chatbot within 'Physical AI and Humanoid Robotics'.
This chatbot, utilizing the OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier, must be able to answer user questions about the book's content, including answering questions based only on text selected by the user.
Answer with simple language s everyone can understand it.
```

## Response snapshot

Updated the project constitution to include requirements for the RAG chatbot integration while maintaining the educational focus on Physical AI and Humanoid Robotics. Added new principles VII and VIII specifically addressing RAG chatbot integration and technology stack standards. Modified existing principles to ensure content is structured for effective RAG system processing while maintaining educational effectiveness.

## Outcome

- ✅ Impact: Updated constitution to include RAG chatbot requirements and technology stack standards
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated
- 🔁 Next prompts: Plan RAG chatbot architecture, implement RAG system components
- 🧠 Reflection: Successfully integrated technical requirements with educational content needs

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Begin RAG system implementation