import uvicorn
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.middleware.metrics import metrics_middleware

app=FastAPI(title='Automated Retirement Savings', version="1.0.0")
app.middleware("http")(metrics_middleware)
app.include_router(api_router, prefix="/api/v1")

