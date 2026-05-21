import numpy as np

import app.rag.vector_store as vector_store

from app.rag.embeddings import (
    generate_embeddings
)


def retrieve_documents(
    query,
    top_k=5
):

    if vector_store.index is None:

        raise ValueError(
            "Vector store is not initialized"
        )

    query_embedding = generate_embeddings(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = vector_store.index.search(
        query_embedding,
        top_k
    )

    retrieved_docs = []

    # RELAXED THRESHOLD
    DISTANCE_THRESHOLD = 8.0

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        if (
            idx >= 0 and
            idx < len(
                vector_store.metadata_store
            )
            and
            distance < DISTANCE_THRESHOLD
        ):

            retrieved_docs.append(
                vector_store.metadata_store[idx]
            )

    # FALLBACK SAFETY
    # If nothing retrieved,
    # return top chunks anyway
    if not retrieved_docs:

        for idx in indices[0]:

            if (
                idx >= 0 and
                idx < len(
                    vector_store.metadata_store
                )
            ):

                retrieved_docs.append(
                    vector_store.metadata_store[idx]
                )

    return retrieved_docs