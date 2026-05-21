from fastapi import APIRouter

from app.services.suggestion_service import (
    get_suggestions
)


router = APIRouter()


@router.get("/suggestions")
async def fetch_suggestions():

    suggestions = get_suggestions()

    return {
        "suggestions": suggestions
    }