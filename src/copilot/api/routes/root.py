from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    """Root endpoint for the API."""
    return {
        "name": "Enterprise Engineering Copilot",
        "version": "1.0.0",
        "status": "running"
    }
