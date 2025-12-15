# Running the Physical AI & Humanoid Robotics RAG Chatbot

This guide explains how to run the complete RAG chatbot system with both backend and frontend components.

## Prerequisites

- Python 3.10+ installed
- Node.js and npm installed
- OpenAI API key
- Qdrant Cloud account and API key (or local Qdrant instance)

## Step 1: Backend Setup (Chatbot API)

1. **Navigate to the chatbot directory:**
   ```bash
   cd chat-bot
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy the example environment file: `cp .env.example .env`
   - Edit `.env` and add your API keys:
     ```
     OPENAI_API_KEY=your_actual_openai_api_key
     QDRANT_URL=your_qdrant_cluster_url
     QDRANT_API_KEY=your_qdrant_api_key
     NEON_DATABASE_URL=your_neon_postgres_connection_string
     ```

4. **Initialize the system:**
   ```bash
   python setup.py
   ```
   This will:
   - Set up the database tables
   - Load and embed all book content into the vector store

5. **Start the backend server:**
   ```bash
   python -m chat-bot.backend.main
   ```
   The API will start on `http://localhost:8000`

## Step 2: Frontend Setup (Docusaurus Integration)

1. **Open a new terminal/command prompt**
2. **Navigate to the my-book directory:**
   ```bash
   cd my-book
   ```

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Start the Docusaurus development server:**
   ```bash
   npm start
   ```
   The website will start on `http://localhost:3000`

## Step 3: Using the Chatbot

1. **Access your book:** Open `http://localhost:3000` in your browser
2. **Find the chatbot:** Look for the chatbot icon (🤖) in the bottom-right corner
3. **Start chatting:** Click the icon and ask questions about Physical AI & Humanoid Robotics
4. **Use context:** Select text on any page and then ask questions about that specific content

## Troubleshooting

### Backend Issues
- **Database Connection**: Ensure your Neon Postgres URL is correct
- **Qdrant Connection**: Verify Qdrant URL and API key are properly set
- **OpenAI API**: Check that your OpenAI API key is valid and has sufficient credits

### Frontend Issues
- **Chatbot not appearing**: Make sure you started both backend and frontend servers
- **API Connection Errors**: Verify both servers are running and the API URL is correct
- **CORS Issues**: The backend allows all origins in development mode

### Environment Variables
Make sure all required environment variables are set in both:
- `chat-bot/.env` for the backend
- `my-book/.env` for the frontend (if needed)

## Production Deployment

For production deployment:

1. **Backend**: Deploy to a cloud provider (AWS, GCP, Azure, etc.) with proper security
2. **Database**: Use production-ready Neon Postgres instance
3. **Vector Store**: Use production Qdrant Cloud cluster
4. **Frontend**: Build and deploy the Docusaurus site with `npm run build`

## Stopping the Servers

To stop the servers:
- Press `Ctrl+C` in each terminal where the servers are running

## Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Docusaurus    │    │   FastAPI API    │    │  External APIs  │
│   Frontend      │◄──►│   (chat-bot/)    │◄──►│  (OpenAI, etc)  │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
            ┌───────▼────────┐  ┌───────▼────────┐
            │  Neon Postgres │  │   Qdrant DB    │
            │   (Sessions)   │  │  (Book Content)│
            └────────────────┘  └────────────────┘
```

The chatbot is now ready to use! It will appear as a floating widget on all pages of your Docusaurus-based book, allowing users to ask questions about the Physical AI & Humanoid Robotics content.