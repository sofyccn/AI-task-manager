from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(TITLE="Task-Manager-API")

#Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
