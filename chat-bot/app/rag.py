from dotenv import load_dotenv
import os
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EMBEDDING_DIM = 768 # text-embedding-004

class RAGEngine:
    def __init__(self):
        if not GEMINI_API_KEY:
             raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        print(f"[RAG] Connecting to Qdrant at {QDRANT_URL}...")
        try:
            # Try connecting with a timeout
            self.qdrant = QdrantClient(
                url=QDRANT_URL,
                api_key=QDRANT_API_KEY if QDRANT_API_KEY else None,
                timeout=5.0 
            )
            # Test connection by listing collections
            self.qdrant.get_collections()
            print("[RAG] Connected to Qdrant successfully.")
        except Exception as e:
            print(f"[RAG] ⚠️ Could not connect to Qdrant at {QDRANT_URL}: {e}")
            print("[RAG] ⚠️ Falling back to IN-MEMORY Qdrant (Non-persistent).")
            self.qdrant = QdrantClient(":memory:")
            
        self._ensure_collection()
    
    def _ensure_collection(self):
        """Create collection if it doesn't exist"""
        try:
            collections = self.qdrant.get_collections().collections
            if not any(c.name == COLLECTION_NAME for c in collections):
                print(f"[RAG] Creating collection: {COLLECTION_NAME}")
                self.qdrant.create_collection(
                    collection_name=COLLECTION_NAME,
                    vectors_config=VectorParams(
                        size=EMBEDDING_DIM,
                        distance=Distance.COSINE
                    )
                )
                print("[RAG] Collection created.")
            else:
                print(f"[RAG] Collection {COLLECTION_NAME} already exists.")
        except Exception as e:
            print(f"[RAG] Error ensuring collection: {e}")
            pass
    
    async def embed_query(self, text: str) -> List[float]:
        """Generate embedding for query text"""
        print(f"[RAG] Generating embedding for text: {text[:50]}...")
        # Native Gemini Embedding
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_query"
        )
        print("[RAG] Embedding generated via text-embedding-004")
        return result['embedding']
    
    async def search_vectors(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search Qdrant for similar chunks"""
        try:
            print(f"[RAG] Searching Qdrant for: {query[:50]}...")
            query_vector = await self.embed_query(query)
            results = self.qdrant.search(
                collection_name=COLLECTION_NAME,
                query_vector=query_vector,
                limit=top_k
            )
            print(f"[RAG] Found {len(results)} chunks in Qdrant")
            return [
                {
                    "text": hit.payload.get("text", "")[:500],  # Limit chunk size
                    "chapter": hit.payload.get("chapter", "Unknown"),
                    "score": hit.score
                }
                for hit in results
            ]
        except Exception as e:
            print(f"[RAG] Vector search error: {e}")
            return []
    
    def build_prompt(self, question: str, context_chunks: List[Dict]) -> str:
        """Build concise prompt with retrieved context"""
        if context_chunks:
            context = "\n".join([
                f"[{c.get('chapter', '')}]: {c.get('text', '')}" 
                for c in context_chunks
            ])
            return f"""You are a robotics tutor. Answer concisely in 2-3 sentences.

Context:
{context}

Q: {question}
A:"""
        else:
            return f"""You are a robotics tutor. Answer concisely in 2-3 sentences about ROS2, Gazebo, Isaac Sim, or VLA.

Q: {question}
A:"""

    async def generate_answer(self, prompt: str) -> str:
        """Generate answer using Gemini 1.5 Flash"""
        print(f"[RAG] Calling Gemini 1.5 Flash")
        # Native Gemini generation
        response = await self.model.generate_content_async(prompt)
        print("[RAG] Gemini response received")
        return response.text
    
    async def ask(self, question: str) -> Dict[str, Any]:
        """Full RAG pipeline: embed → search → generate"""
        print(f"[RAG] Processing question: {question}")
        # Search for relevant chunks (reduced to 3)
        chunks = await self.search_vectors(question, top_k=3)
        
        # Build prompt with context
        prompt = self.build_prompt(question, chunks)
        
        # Generate answer
        answer = await self.generate_answer(prompt)
        
        # Build sources
        sources = [
            {"chapter": c["chapter"], "score": round(c["score"], 3)}
            for c in chunks if c.get("score", 0) > 0.0  # Lower threshold as metrics might differ
        ]
        
        return {
            "answer": answer,
            "sources": sources
        }
    
    async def ask_selection(self, question: str, selection: str) -> Dict[str, Any]:
        """Answer question about selected text (no RAG)"""
        print(f"[RAG] Processing selection request")
        # Limit selection to 500 chars
        selection = selection[:500]
        prompt = f"""Explain this text concisely in 2-3 sentences:

Text: {selection}

Q: {question}
A:"""

        answer = await self.generate_answer(prompt)
        return {"answer": answer}
    
    async def index_chunk(self, chunk_id: str, text: str, chapter: str):
        """Index a single chunk into Qdrant"""
        embedding = await self.embed_query(text)
        self.qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=hash(chunk_id) % (2**63),
                    vector=embedding,
                    payload={"text": text, "chapter": chapter, "chunk_id": chunk_id}
                )
            ]
        )

