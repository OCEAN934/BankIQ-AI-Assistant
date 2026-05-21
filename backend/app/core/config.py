from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = "BankIQ AI Assistant"
    VERSION = "1.0.0"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)
    EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

    RAW_DATA_PATH = "app/data/raw"
    VECTOR_STORE_PATH = "app/data/vector_store"

settings = Settings()