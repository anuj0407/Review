from fastapi import FastAPI
from routes import router as prod_router

app = FastAPI()

app.include_router(prod_router)

