from fastapi import FastAPI
from routes.user_routes import router as user_router

# RUN: uvicorn main:app --reload

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "api is running"}