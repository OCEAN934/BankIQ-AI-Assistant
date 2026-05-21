from app.utils.file_parser import parse_document
from app.rag.chunking import create_chunks
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import (
    add_embeddings,
    save_vector_store
)

def ingest_document(file_path, filename):
    parsed_docs = parse_document(file_path)

    chunks = create_chunks(parsed_docs, filename)

    texts = [chunk["content"] for chunk in chunks]

    embeddings = generate_embeddings(texts)

    metadata = []

    for chunk in chunks:
        metadata.append(
            {
                "content": chunk["content"],
                "source": chunk["metadata"]["source"],
                "page": chunk["metadata"]["page"]
            }
        )

    add_embeddings(embeddings, metadata)

    save_vector_store()