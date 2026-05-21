from sentence_transformers import CrossEncoder


reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_documents(query, documents, top_k=5):

    pairs = []

    for doc in documents:
        pairs.append((query, doc["content"]))

    scores = reranker_model.predict(pairs)

    scored_docs = list(zip(documents, scores))

    scored_docs = sorted(
        scored_docs,
        key=lambda x: x[1],
        reverse=True
    )

    reranked = []

    for doc, score in scored_docs[:top_k]:

        doc["rerank_score"] = float(score)

        reranked.append(doc)

    return reranked