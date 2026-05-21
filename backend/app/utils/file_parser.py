from pypdf import PdfReader
from pathlib import Path


def parse_pdf(file_path: str):
    reader = PdfReader(file_path)

    pages = []

    for idx, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            pages.append(
                {
                    "page": idx + 1,
                    "text": text
                }
            )

    return pages

def parse_txt(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [
        {
            "page": 1,
            "text": text
        }
    ]

def parse_document(file_path: str):
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return parse_pdf(file_path)

    elif extension == ".txt":
        return parse_txt(file_path)

    else:
        raise ValueError("Unsupported file format")