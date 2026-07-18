from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    """Health check endpoint for the API."""
    return {"status": "healthy", "message": "The API is running smoothly."}
