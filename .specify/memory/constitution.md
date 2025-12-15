<!-- SYNC IMPACT REPORT
Version change: 1.1.0 → 1.2.0
Modified principles: I, II, III, IV, V, VI (expanded to include RAG chatbot integration requirements)
Added sections: VII. RAG Chatbot Integration, VIII. Technology Stack Standards
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ updated
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics RAG Chatbot Constitution

## Core Principles

### I. Educational Structure and Progression
The course/book must be divided into 4 modules with a short course introduction, followed by lessons and quizzes. Each module must contain relevant lessons plus one quiz. The modules must be: 1) ROS2 basics, 2) Digital Twin (Gazebo + Unity), 3) NVIDIA Isaac Sim, 4) Vision-Language-Action. The course must start with a short course introduction explaining the overall structure and objectives. The content must be structured in a way that enables effective retrieval and understanding by the RAG chatbot system.

### II. Accessibility and Clarity
All writing must use simple, clear, human-friendly language that even beginners can understand. Technical accuracy, clarity, and educational usefulness must be maintained throughout. The course content must maintain conceptual depth without overwhelming the reader. The tone must stay encouraging, friendly, and motivating. Content must be structured with clear headings, paragraphs, and semantic organization to facilitate RAG system parsing and retrieval.

### III. Visual Design Excellence
Visual feel must be strong with clean fonts, pleasant color themes (described textually), and easy-to-read formatting. All content must be designed with strong visual appeal to enhance learning experience and reader engagement. Visual elements must be appropriately tagged and described to enable RAG system indexing and retrieval.

### IV. Sequential Learning Path
Module progression must follow the established sequence: ROS2 basics → Digital Twin → NVIDIA Isaac Sim → Vision-Language-Action. Each module must build logically on the previous one, ensuring a coherent learning journey from foundational ROS2 concepts to advanced AI integration systems. Content chunks must maintain logical flow and context for effective RAG retrieval and generation.

### V. Content Quality and Accuracy
Technical accuracy, clarity, and educational usefulness must be maintained throughout. All content must be factually correct, pedagogically sound, and practically valuable to readers at each level. Content must be consistently formatted and structured to enable reliable RAG system processing and retrieval.

### VI. Comprehensive Coverage
Additional helpful or valuable topics may be added when beneficial. The course must cover Physical AI and Humanoid Robotics comprehensively through the specified technology modules, providing readers with practical knowledge across the major tools and frameworks. Content must be organized in digestible, semantically coherent segments suitable for RAG system chunking and retrieval.

### VII. RAG Chatbot Integration
The integrated RAG chatbot must be built using OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier. The system must be able to answer user questions about the book's content with high accuracy and relevance. The chatbot must be able to respond to questions based only on text selected by the user, ensuring factual accuracy and preventing hallucinations. All content must be properly indexed, vectorized, and retrievable to support effective question-answering capabilities.

### VIII. Technology Stack Standards
The RAG system must utilize OpenAI Agents/ChatKit SDKs for intelligent interaction, FastAPI for efficient backend services, Neon Serverless Postgres for structured metadata storage, and Qdrant Cloud for vector similarity search. All components must be properly integrated and secured, following industry best practices for data privacy and system reliability.

## Educational Standards

The course content must guide readers from foundational ROS2 concepts to advanced AI integration using an easy, approachable writing style. Each lesson must include clear learning objectives, practical examples, and concept reinforcement through quizzes. All content must be structured to maximize learning retention and understanding. Content must be formatted and segmented to support RAG system retrieval while maintaining educational effectiveness for human readers.

## Development Workflow

Content creation must follow the established structure: Course Introduction → 4 Modules → (Each with lessons + quiz). Each module and lesson must be reviewed for adherence to the educational standards, structural requirements, and accessibility principles. Quality gates include technical accuracy verification, readability assessment, visual design compliance, and RAG system compatibility evaluation. All content must be tested with the RAG system to ensure proper indexing and retrieval.

## Governance

This constitution governs all content creation and structural decisions for the Physical AI & Humanoid Robotics course and its integrated RAG chatbot system. All additions, modifications, and reviews must comply with these principles. Amendments require documentation of the change, justification for deviation from established structure, and approval from project leadership. Changes affecting the RAG system must include impact assessment on retrieval accuracy and user experience.

**Version**: 1.2.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-07