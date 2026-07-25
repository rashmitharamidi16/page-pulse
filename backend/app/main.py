from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Page Pulse API",
    description="Website auditing service",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Page Pulse API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }