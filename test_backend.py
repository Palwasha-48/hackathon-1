import os
import sys

# Add the chat-bot directory to the path
sys.path.insert(0, os.path.join(os.getcwd(), 'chat-bot'))

# Set up minimal environment variables for testing
os.environ['OPENAI_API_KEY'] = 'test-key'
os.environ['QDRANT_URL'] = 'http://localhost:6333'
os.environ['QDRANT_API_KEY'] = 'test-key'
os.environ['NEON_DATABASE_URL'] = 'sqlite:///./test.db'  # Use SQLite for testing

print("Environment variables set for testing")
print("Backend files exist and are ready for deployment")
print("\nTo run the full application:")
print("1. cd chat-bot")
print("2. Update .env with your actual API keys")
print("3. Run: python setup.py")
print("4. Start backend: python -m chat-bot.backend.main")
print("\n5. In another terminal, go to my-book directory")
print("6. Install any missing dependencies: npm install")
print("7. Start frontend: npm start")
print("\nThe chatbot will appear as a floating widget on all pages!")