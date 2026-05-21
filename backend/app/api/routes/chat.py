from fastapi import APIRouter

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from app.services.memory_service import (
    add_message,
    get_conversation
)

from app.rag.query_rewriter import rewrite_query

from app.rag.retriever import retrieve_documents

from app.rag.reranker import rerank_documents

from app.rag.response_generator import generate_response

from app.rag.citation_handler import generate_sources


router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    conversation = get_conversation(
        request.session_id
    )

    rewritten_query = rewrite_query(
        request.query,
        conversation
    )

    retrieved_docs = retrieve_documents(
        rewritten_query,
        top_k=10
    )

    reranked_docs = rerank_documents(
        request.query,
        retrieved_docs,
        top_k=5
    )

    answer = generate_response(
        request.query,
        reranked_docs
    )

    add_message(
        request.session_id,
        f"User: {request.query}"
    )

    add_message(
        request.session_id,
        f"Assistant: {answer}"
    )

    sources = generate_sources(
        reranked_docs
    )

    # =========================================
    # CONFIDENCE ESTIMATION
    # =========================================

    source_count = len(sources)

    if source_count >= 3:

        confidence = "High"

    elif source_count == 2:

        confidence = "Medium"

    else:

        confidence = "Low"

    return ChatResponse(
        answer=answer,
        sources=sources,
        confidence=confidence
    )