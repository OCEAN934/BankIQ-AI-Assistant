import requests

import os

BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)


def upload_document(file):

    files = {
        "file": (
            file.name,
            file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

    return response.json()


def send_chat_message(session_id, query):

    payload = {
        "session_id": session_id,
        "query": query
    }

    response = requests.post(
        f"{BASE_URL}/chat",
        json=payload
    )

    return response.json()


def fetch_suggestions():

    response = requests.get(
        f"{BASE_URL}/suggestions"
    )

    return response.json()