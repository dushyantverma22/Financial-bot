from fastapi import FastAPI

app = FastAPI(
    title="Portfolio AI Assistant",
    version="1.0"
)

from backened.api.routes.chat import (
    router as chat_router
)
from backened.api.routes.upload import (
    router as upload_router)

from backened.api.routes.portfolio import (
    router as portfolio_router)

app.include_router(
    chat_router
)

app.include_router(
    chat_router
)

app.include_router(
    upload_router
)

app.include_router(
    portfolio_router
)

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }