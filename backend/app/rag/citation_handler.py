def generate_sources(retrieved_docs):

    sources = []

    seen = set()

    for doc in retrieved_docs:

        source_key = (
            doc["source"],
            doc["page"]
        )

        if source_key not in seen:

            seen.add(source_key)

            sources.append(
                {
                    "document": doc["source"],
                    "page": doc["page"]
                }
            )

    return sources