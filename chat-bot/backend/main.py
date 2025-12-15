from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import uuid

# Load environment variables
load_dotenv()

# Import the RAG service
from .rag_service import rag_service

app = FastAPI(title="Physical AI & Humanoid Robotics RAG Chatbot API",
              description="API for the educational chatbot system",
              version="1.0.0")

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    context_text: Optional[str] = None
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    sources: List[str] = []
    session_id: str

# Simple in-memory storage for demonstration
# In a real implementation, you would use a proper database
chat_sessions = {}

# Enhanced chat endpoint with actual RAG functionality
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Generate or use session ID
    session_id = request.session_id or str(uuid.uuid4())

    user_message = request.messages[-1].content if request.messages else 'No message provided'

    # Use the RAG service to get answer
    result = rag_service.get_answer(user_message, request.context_text)

    return ChatResponse(
        response=result["response"],
        sources=result["sources"],
        session_id=session_id
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "RAG Chatbot API", "book_content_docs": len(rag_service.book_content)}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Physical AI & Humanoid Robotics RAG Chatbot API",
            "version": "1.0.0",
            "endpoints": ["/chat", "/health"],
            "book_content_docs": len(rag_service.book_content)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)