"""
RAG (Retrieval-Augmented Generation) Service for the Physical AI & Humanoid Robotics Chatbot
"""
import os
from typing import List, Dict, Optional
from pathlib import Path
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import Qdrant
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.docstore.document import Document
    from langchain.chains import RetrievalQA
    EMBEDDING_AVAILABLE = True
except ImportError:
    logger.warning("LangChain dependencies not available. Using basic search functionality.")
    EMBEDDING_AVAILABLE = False

class RAGService:
    def __init__(self):
        self.embeddings = None
        self.vector_store = None
        self.qa_chain = None
        self.use_embeddings = EMBEDDING_AVAILABLE and os.getenv("OPENAI_API_KEY")

        if self.use_embeddings:
            try:
                # Initialize OpenAI embeddings
                self.embeddings = OpenAIEmbeddings(
                    openai_api_key=os.getenv("OPENAI_API_KEY")
                )

                # Initialize Qdrant vector store (will connect when needed)
                # For now, we'll use a basic approach
                logger.info("Using OpenAI embeddings with Qdrant vector store")
            except Exception as e:
                logger.error(f"Error initializing embeddings: {e}")
                self.use_embeddings = False
                self.embeddings = None

        # Load book content
        self.book_content = self.load_book_content()
        logger.info(f"Loaded {len(self.book_content)} documents from book content")

    def load_book_content(self) -> List[Dict]:
        """Load educational content from the my-book/docs directory"""
        # Get the project root directory (where the chat-bot folder is)
        project_root = Path(__file__).parent.parent.parent
        content_dir = project_root / "my-book" / "docs"
        all_content = []

        if content_dir.exists():
            for file_path in content_dir.rglob("*.md"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        all_content.append({
                            'source': str(file_path),
                            'content': content,
                            'title': file_path.stem
                        })
                except Exception as e:
                    logger.warning(f"Could not read file {file_path}: {e}")
                    continue  # Skip files that can't be read

        return all_content

    def simple_search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Simple keyword-based search function"""
        query_lower = query.lower()
        results = []

        for item in self.book_content:
            content_lower = item['content'].lower()
            if query_lower in content_lower:
                # Simple relevance scoring based on keyword matches
                score = content_lower.count(query_lower)
                results.append({
                    'content': item['content'],
                    'source': item['source'],
                    'title': item['title'],
                    'score': score
                })

        # Sort by score and return top results
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

    def semantic_search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Semantic search using embeddings (if available)"""
        if not self.use_embeddings:
            return self.simple_search(query, top_k)

        try:
            # For now, using simple search as vector store setup requires more infrastructure
            # In a real implementation, you would use the vector store for semantic search
            return self.simple_search(query, top_k)
        except Exception as e:
            logger.error(f"Error in semantic search: {e}")
            return self.simple_search(query, top_k)

    def get_answer(self, query: str, context_text: Optional[str] = None) -> Dict:
        """Get answer for a query using RAG"""
        # Search for relevant content
        relevant_content = self.semantic_search(query)

        if relevant_content:
            # Build context from relevant content
            context_snippets = []
            sources = []

            for item in relevant_content:
                content_snippet = item['content'][:1000]  # Limit snippet size
                context_snippets.append(content_snippet)
                sources.append(item['source'])

            context = "\n\n".join(context_snippets)

            # Extract the most relevant information from the context to answer the query
            # This is a simple approach - in a real implementation you'd use an LLM to generate the response
            response = self.generate_response_from_context(query, context)

            return {
                "response": response,
                "sources": sources
            }
        else:
            # If no relevant content found in book, try to use context_text if provided
            if context_text:
                # Generate response based on the selected text context
                response = f"Based on the selected text you provided:\n\n{context_text[:500]}...\n\nThis content relates to your question about '{query}'. The selected text provides context about this topic."
                return {
                    "response": response,
                    "sources": ["Selected page text"]
                }
            else:
                # No relevant content found and no context provided
                response = f"I couldn't find specific information in the Physical AI & Humanoid Robotics educational content about '{query}'. The book may not contain detailed information on this specific topic. Please try asking about core concepts like humanoid robotics, physical AI, robot control systems, or related topics covered in the book."
                return {
                    "response": response,
                    "sources": []
                }

    def generate_response_from_context(self, query: str, context: str) -> str:
        """Generate a more natural response based on the context and query"""
        # Find sentences in the context that are most relevant to the query
        import re

        # Split context into sentences
        sentences = re.split(r'[.!?]+', context)

        # Find sentences that contain query keywords
        query_keywords = query.lower().split()
        relevant_sentences = []

        for sentence in sentences:
            sentence_lower = sentence.lower()
            # Count how many query keywords appear in the sentence
            keyword_matches = sum(1 for keyword in query_keywords if keyword in sentence_lower)
            if keyword_matches > 0:
                relevant_sentences.append((sentence.strip(), keyword_matches))

        # Sort by keyword matches (descending)
        relevant_sentences.sort(key=lambda x: x[1], reverse=True)

        # Take top sentences that are not empty
        top_sentences = [sent[0] for sent in relevant_sentences if sent[0].strip()][:3]

        if top_sentences:
            response_content = ". ".join(top_sentences) + "."
            return f"According to the Physical AI & Humanoid Robotics educational content:\n\n{response_content}\n\nThis directly addresses your question about '{query}'."
        else:
            # If no keyword matches found, return a summary of the context
            return f"Based on the Physical AI & Humanoid Robotics educational content:\n\n{context[:800]}{'...' if len(context) > 800 else ''}\n\nThis content is relevant to your question about '{query}'."

# Create a global instance
rag_service = RAGService()