import uvicorn
from fastapi import FastAPI

from scripts.core.services.sevice import college_router

app = FastAPI()
app.include_router(college_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8020)
