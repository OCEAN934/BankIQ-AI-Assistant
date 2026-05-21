from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

import shutil
import os

import PyPDF2

from docx import Document

from app.rag.ingest import ingest_document

from app.core.config import settings

from app.services.suggestion_generator import (
    generate_document_suggestions
)

from app.services.suggestion_service import (
    save_suggestions
)

from app.rag.vector_store import (
    reset_vector_store
)

from app.services.memory_service import (
    clear_memory
)


router = APIRouter()


def extract_text_for_suggestions(
    file_path,
    extension
):

    text = ""

    # PDF
    if extension == ".pdf":

        with open(file_path, "rb") as file:

            pdf_reader = PyPDF2.PdfReader(
                file
            )

            for page in pdf_reader.pages[:5]:

                extracted = page.extract_text()

                if extracted:

                    text += (
                        extracted + "\n"
                    )

    # TXT
    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            text = file.read()

    # DOCX
    elif extension == ".docx":

        document = Document(file_path)

        for para in document.paragraphs:

            text += para.text + "\n"

    return text


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    allowed_extensions = [
        ".pdf",
        ".txt",
        ".docx"
    ]

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail=(
                "Only PDF, TXT and DOCX "
                "files are supported"
            )
        )

    # CLEAR OLD DATA
    reset_vector_store()

    clear_memory()

    save_suggestions([])

    # REMOVE OLD RAW FILES
    if os.path.exists(
        settings.RAW_DATA_PATH
    ):

        for existing_file in os.listdir(
            settings.RAW_DATA_PATH
        ):

            existing_path = os.path.join(
                settings.RAW_DATA_PATH,
                existing_file
            )

            if os.path.isfile(existing_path):

                os.remove(existing_path)

    save_path = (
        f"{settings.RAW_DATA_PATH}/"
        f"{file.filename}"
    )

    os.makedirs(
        settings.RAW_DATA_PATH,
        exist_ok=True
    )

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # INGEST CURRENT FILE ONLY
    ingest_document(
        save_path,
        file.filename
    )

    # GENERATE NEW SUGGESTIONS
    try:

        extracted_text = (
            extract_text_for_suggestions(
                save_path,
                extension
            )
        )

        suggestions = (
            generate_document_suggestions(
                extracted_text
            )
        )

        save_suggestions(
            suggestions
        )

    except Exception as e:

        print(
            "Suggestion generation failed:",
            e
        )

    return {
        "message":
        "Document uploaded and indexed successfully",
        "filename": file.filename
    }