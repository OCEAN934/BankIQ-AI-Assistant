import faiss
import numpy as np
import pickle
import os

from app.core.config import settings


index = None
metadata_store = []


def initialize_vector_store(dimension=384):

    global index
    global metadata_store

    index = faiss.IndexFlatL2(dimension)

    metadata_store = []


def reset_vector_store():

    global index
    global metadata_store

    index = faiss.IndexFlatL2(384)

    metadata_store = []

    # DELETE OLD VECTOR FILES
    index_path = (
        f"{settings.VECTOR_STORE_PATH}/faiss.index"
    )

    metadata_path = (
        f"{settings.VECTOR_STORE_PATH}/metadata.pkl"
    )

    if os.path.exists(index_path):

        os.remove(index_path)

    if os.path.exists(metadata_path):

        os.remove(metadata_path)


def add_embeddings(embeddings, metadata):

    global index
    global metadata_store

    embeddings = np.array(
        embeddings
    ).astype("float32")

    index.add(embeddings)

    metadata_store.extend(metadata)


def save_vector_store():

    os.makedirs(
        settings.VECTOR_STORE_PATH,
        exist_ok=True
    )

    faiss.write_index(
        index,
        f"{settings.VECTOR_STORE_PATH}/faiss.index"
    )

    with open(
        f"{settings.VECTOR_STORE_PATH}/metadata.pkl",
        "wb"
    ) as file:

        pickle.dump(
            metadata_store,
            file
        )


def load_vector_store():

    global index
    global metadata_store

    index_path = (
        f"{settings.VECTOR_STORE_PATH}/faiss.index"
    )

    metadata_path = (
        f"{settings.VECTOR_STORE_PATH}/metadata.pkl"
    )

    if os.path.exists(index_path):

        index = faiss.read_index(
            index_path
        )

    else:

        initialize_vector_store()

    if os.path.exists(metadata_path):

        with open(metadata_path, "rb") as file:

            metadata_store = pickle.load(file)

    else:

        metadata_store = []