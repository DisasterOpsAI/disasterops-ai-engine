from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DisasterOps AI Engine",
    description="A Python/FastAPI monolith encapsulating all ML pipelines and agent workflows—damage assessment, resource-allocation recommendations, alert generation, and multimodal data inference.",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "DisasterOps AI Engine is running",
        "status": "healthy",
        "version": "0.1.0",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "0.1.0",
        "message": "DisasterOps AI Engine is operational",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
