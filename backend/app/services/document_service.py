from PyPDF2 import PdfReader

from docx import Document


def load_document(file_path):

    if file_path.endswith(".pdf"):

        return load_pdf(file_path)

    elif file_path.endswith(".txt"):

        return load_txt(file_path)

    elif file_path.endswith(".docx"):

        return load_docx(file_path)

    else:

        raise ValueError(
            "Unsupported file format"
        )


def load_pdf(file_path):

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            documents.append({
                "content": text,
                "page": page_number + 1
            })

    return documents


def load_txt(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    return [
        {
            "content": text,
            "page": 1
        }
    ]


def load_docx(file_path):

    doc = Document(file_path)

    full_text = []

    for para in doc.paragraphs:

        if para.text.strip():

            full_text.append(
                para.text
            )

    text = "\n".join(full_text)

    return [
        {
            "content": text,
            "page": 1
        }
    ]