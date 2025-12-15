import asyncio
import os
from dotenv import load_dotenv

# Force load the backend .env file
load_dotenv(dotenv_path=".env")

print("--- Environment Check ---")
print(f"GEMINI_API_KEY present: {'Yes' if os.getenv('GEMINI_API_KEY') else 'No'}")
print(f"QDRANT_URL: {os.getenv('QDRANT_URL')}")

print("\n--- Importing RAGEngine ---")
try:
    from app.rag import RAGEngine
except ImportError as e:
    print(f"❌ Error importing RAGEngine: {e}")
    print("Do you have 'google-generativeai' installed? Run: pip install google-generativeai")
    exit(1)

async def test_logic():
    print("\n--- Initializing RAGEngine ---")
    try:
        rag = RAGEngine()
        print("✅ RAGEngine initialized.")
    except Exception as e:
        print(f"❌ RAGEngine Init Failed: {e}")
        return

    question = "What is ROS2?"
    selection = "ROS2 is the Robot Operating System."
    
    print(f"\n--- Testing ask_selection ---\nQuestion: {question}\nSelection: {selection}")
    try:
        # Test ask_selection (since that's what was hanging in the logs)
        result = await rag.ask_selection(question, selection)
        print("\n✅ Result Recieved:")
        print(result)
    except Exception as e:
        print(f"\n❌ ask_selection Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_logic())
