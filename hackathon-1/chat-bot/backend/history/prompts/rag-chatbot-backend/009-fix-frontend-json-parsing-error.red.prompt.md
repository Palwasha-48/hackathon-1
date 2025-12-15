---
id: 009
title: "Fix Frontend JSON Parsing Error"
stage: "red"
date: "2025-12-10"
surface: "agent"
model: "qwen3-coder-plus"
feature: "rag-chatbot-backend"
branch: "main"
user: "unknown"
command: "/sp.phr"
labels: ["debugging", "frontend", "api-integration", "json-parsing", "proxy-configuration"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "my-book/src/components/Chatbot/ChatbotWidget.jsx"
tests:
  - "none"
---

# Fix Frontend JSON Parsing Error

## Prompt Text
```
/sp.implement
Fix the frontend JSON parsing error: `Unexpected token '<', "<!DOCTYPE "... is not valid JSON`.
**Root Cause:**
The frontend [ChatbotWidget.jsx](cci:7://file:///F:/Courses/Hamza/hackathon_2_phase-2/hackathon-1/my-book/src/components/Chatb
ot/ChatbotWidget.jsx:0:0-0:0) is making requests to relative paths (e.g., `/api/ask`), which resolve to the Docusaurus dev
server (`http://localhost:3000`). Since the proxy configuration was removed from
[docusaurus.config.ts](cci:7://file:///F:/Courses/Hamza/hackathon_2_phase-2/hackathon-1/my-book/docusaurus.config.ts:0:0-0:0),
 these requests return the 404 HTML page instead of JSON from the backend.
**Required Fix:**
1. Update [my-book/src/components/Chatbot/ChatbotWidget.jsx](cci:7://file:///F:/Courses/Hamza/hackathon_2_phase-2/hackathon-1/
my-book/src/components/Chatbot/ChatbotWidget.jsx:0:0-0:0) to use the full backend URL (`http://localhost:8000`) for API calls.
2. Define a `API_BASE_URL` constant that points to `http://localhost:8000`.
```

## Response Text
Fixed the frontend JSON parsing error by updating ChatbotWidget.jsx to use full backend URL instead of relative paths. Added API_BASE_URL constant and updated API calls to use http://localhost:8000/api/ask and http://localhost:8000/api/ask-selection.

## Outcome Impact
Resolved the "Unexpected token '<', '<!DOCTYPE '... is not valid JSON" error by ensuring API calls go directly to the backend server instead of resolving to the Docusaurus dev server where no proxy exists.

## Tests Summary
Verified that both API endpoints are accessible at http://localhost:8000/api/ask and http://localhost:8000/api/ask-selection

## Files Summary
- my-book/src/components/Chatbot/ChatbotWidget.jsx: Added API_BASE_URL constant and updated fetch calls to use full URLs

## Next Prompts
none

## Reflection Note
Using absolute URLs instead of relative paths is essential when proxy configuration is removed from the frontend framework.

---
## Evaluation Notes

**Failure modes observed:** None
**Next experiment to improve prompt quality:** None needed - fix was successful and complete.
---