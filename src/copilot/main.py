from fastapi import FastAPI

from copilot.api.routes.root import router as root_router
from copilot.api.routes.health import router as health_router

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="Enterprise Engineering Copilot", version="1.0.0")

    # Include routers
    app.include_router(root_router)
    app.include_router(health_router)

    return app

app = create_app()