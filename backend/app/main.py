from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.chat import router as chat_router

from app.api.routes.health import router as health_router
from app.api.routes.upload import router as upload_router
from app.api.routes.suggestions import router as suggestions_router


from app.rag.vector_store import (
    initialize_vector_store,
    load_vector_store
)

app = FastAPI(
    title="BankIQ AI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    initialize_vector_store()
    load_vector_store()


app.include_router(health_router)
app.include_router(upload_router)
app.include_router(suggestions_router)
app.include_router(chat_router)
app.include_router(suggestions_router)