from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth

app = FastAPI(
    title="Task Manager API",
    description="AI-Powered Task Management System",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {
        "message": "Task Manager API is running!",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
