# BankIQ AI Assistant

Enterprise-grade AI-powered Banking Intelligence Assistant built using Retrieval-Augmented Generation (RAG), FAISS Vector Search, Cross-Encoder Reranking, and LLM-based grounded reasoning.

BankIQ enables users to upload banking, insurance, and financial policy documents and instantly interact with them through a conversational AI interface that provides contextual answers, source citations, confidence scoring, and intelligent follow-up suggestions.

---

## Live Demo

Frontend Application:

[Add Frontend Deployment URL Here]

Backend API:

[Add Backend Deployment URL Here]

---

## Demo Video

[Add Demo Video Link Here]

---

## Problem Statement

Financial and policy documents are often lengthy, complex, and difficult for customers to navigate.

Traditional keyword search fails to understand intent, context, and relationships between policy clauses.

BankIQ addresses this challenge by combining:

- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Context-Aware Conversations
- Grounded Responses
- Source Attribution

to deliver accurate and explainable answers directly from uploaded documents.

---
## Key Capabilities

| Feature | Description |
|----------|-------------|
| RAG Pipeline | Grounded responses using retrieved document context |
| FAISS Vector Search | Semantic retrieval of relevant document chunks |
| Cross-Encoder Reranking | Improves retrieval precision before generation |
| Conversation Memory | Supports contextual follow-up questions |
| Dynamic Suggestions | Auto-generated document-specific starter questions |
| Confidence Scoring | Indicates reliability of generated responses |
| Source Citations | Provides traceability and explainability |
| Multi-Format Upload | Supports PDF, TXT and DOCX documents |

# Key Features

### Multi-Document Upload

Supports:

- PDF
- TXT
- DOCX

Users can upload documents and instantly start querying them.

<img width="1366" height="1007" alt="screencapture-localhost-8501-2026-05-21-18_57_10" src="https://github.com/user-attachments/assets/d91202f1-3268-41e3-8e42-fe681adafdba" />


---

### Semantic Retrieval using FAISS

Documents are:

1. Parsed
2. Chunked
3. Embedded
4. Indexed in FAISS

Relevant content is retrieved using vector similarity search.

---

### Cross-Encoder Reranking

Retrieved chunks are reranked using:

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

This significantly improves retrieval precision and answer quality.

---

### Conversational AI Chat

Supports:

- Multi-turn conversations
- Context-aware follow-up questions
- Session memory

<img width="682" height="537" alt="image" src="https://github.com/user-attachments/assets/051715c9-d358-415b-94d2-de87d9e12c5f" />


---

### Source Citations

Every response is grounded using retrieved document evidence.

Users can verify where information originated.

<img width="685" height="511" alt="image" src="https://github.com/user-attachments/assets/185c859c-2342-47ff-81fd-db844ccbc3c8" />


---

### Confidence Scoring

Each response includes:

- High Confidence
- Medium Confidence
- Low Confidence

based on supporting evidence available in retrieved sources.

<img width="937" height="450" alt="image" src="https://github.com/user-attachments/assets/2bcff8a0-33f0-40c6-bca6-a7e8151be104" />


---

### Intelligent Suggested Questions

The system automatically generates document-specific starter questions after upload.

Suggestions adapt dynamically to uploaded content.

<img width="1356" height="364" alt="image" src="https://github.com/user-attachments/assets/a0599a8e-c028-40be-87e2-0dc3257c2708" />


---

### Hallucination Reduction

The assistant is explicitly constrained to:

- Use only retrieved context
- Avoid unsupported assumptions
- Indicate when information is unavailable
- Provide grounded reasoning

---

# System Architecture

<img width="2764" height="4564" alt="image" src="https://github.com/user-attachments/assets/75ad6f9a-04de-40be-8aa2-fefd678f781a" />

### Architecture Highlights

- FastAPI backend for scalable API serving
- FAISS vector database for semantic search
- SentenceTransformer embeddings for dense retrieval
- CrossEncoder reranking layer for improved relevance
- Groq-powered LLM reasoning engine
- Streamlit frontend for interactive document intelligence
- Citation and confidence generation layer for explainability

---

## Processing Pipeline

```text
User Uploads Document
        ↓
Document Parsing
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Indexing
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Cross-Encoder Reranking
        ↓
Prompt Construction
        ↓
LLM Response Generation
        ↓
Confidence Estimation
        ↓
Source Attribution
        ↓
Final Response
```

---

# Technology Stack

## Frontend

- Streamlit
- Custom CSS
- Requests

## Backend

- FastAPI
- Pydantic
- Python

## Retrieval Layer

- FAISS
- Sentence Transformers
- LangChain

## Ranking Layer

- CrossEncoder (Sentence Transformers)

## LLM Layer

- Groq API

---

# Project Structure

```text
BankIQ-AI-Assistant
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── rag
│   │   ├── services
│   │   ├── utils
│   │   └── models
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   ├── components
│   ├── services
│   ├── assets
│   ├── app.py
│   └── requirements.txt
│
├── docs
│   ├── architecture_diagram.png
│   └── api_flow.png
│
├── demo
│   └── demo_script.md
│
├── tests
│
├── README.md
└── LICENSE
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/OCEAN934/BankIQ-AI-Assistant.git

cd BankIQ-AI-Assistant
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Create:

```env
backend/.env
```

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

Frontend:

```text
http://localhost:8501
```

---

# API Endpoints

## Upload Document

```http
POST /upload
```

Uploads and indexes documents.

---

## Chat

```http
POST /chat
```

Returns:

- grounded response
- citations
- confidence score

---

## Suggestions

```http
GET /suggestions
```

Returns dynamically generated document-specific questions.

---

## Health Check

```http
GET /health
```

Checks API status.

---

# Example Use Cases

### Banking Policies

- Loan Agreements
- Account Terms
- Credit Card Policies

### Insurance Policies

- Home Insurance
- Life Insurance
- Property Insurance

### Customer Support Knowledge Bases

- FAQs
- Product Documentation
- Compliance Documents

---
# System Innovations

Unlike a traditional chatbot, BankIQ incorporates several advanced retrieval and grounding mechanisms:

- Cross-Encoder Reranking to improve retrieval relevance
- Dynamic document-specific question generation
- Confidence estimation based on supporting evidence
- Context-aware conversation memory
- Structured answer generation for policy reasoning
- Source-backed responses for transparency and trust
- Hallucination reduction through strict context grounding

These enhancements significantly improve answer quality, explainability, and user trust.

# Evaluation Highlights

Implemented:

-> Retrieval-Augmented Generation (RAG)

-> FAISS Vector Database

-> Semantic Search

-> Cross-Encoder Reranking

-> Context-Aware Memory

-> Confidence Scoring

-> Dynamic Suggestions

-> Source Citations

-> Hallucination Reduction

-> Multi-Document Support

-> Streamlit Frontend

-> FastAPI Backend

---
# Results

The system was evaluated on complex banking and insurance policy documents and demonstrated:

- Accurate semantic retrieval using FAISS
- Strong citation-backed responses
- Reduced hallucinations through grounded prompting
- Effective handling of multi-clause policy reasoning
- Dynamic question generation tailored to uploaded documents
- Confidence-aware response generation

The architecture successfully supports document intelligence workflows for banking, insurance, compliance, and customer-support use cases.
---

# Future Improvements

- Multi-document comparison
- OCR support for scanned PDFs
- Authentication and user management
- Citation highlighting inside source documents
- Hybrid Retrieval (BM25 + Dense Retrieval)
- Real-time streaming responses
- Redis caching
- Analytics dashboard

---

# License

This project is licensed under the MIT License.
