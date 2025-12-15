"""
Simple script to run the chatbot backend server
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.main import app
import uvicorn

if __name__ == "__main__":
    print("Starting Physical AI & Humanoid Robotics RAG Chatbot API...")
    print("API will be available at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)