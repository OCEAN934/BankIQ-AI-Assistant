from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=250,

    separators=[
        "\n\n",
        "\n",
        ". ",
        "; ",
        " "
    ]
)


def create_chunks(documents, filename):

    chunks = []

    for doc in documents:

        splits = text_splitter.split_text(
            doc["text"]
        )

        for split in splits:

            cleaned_split = split.strip()

            if len(cleaned_split) < 80:
                continue

            chunks.append(
                {
                    "content": cleaned_split,
                    "metadata": {
                        "source": filename,
                        "page": doc["page"]
                    }
                }
            )

    return chunks