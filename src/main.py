"""Main application entry point."""
import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/ready")
async def ready():
    return {"status": "ready"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
