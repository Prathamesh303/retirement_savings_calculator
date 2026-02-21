from fastapi import APIRouter
from app.api.v1.endpoints import performance,returns,transactions

api_router = APIRouter()
api_router.include_router(transactions.router)
api_router.include_router(returns.router)
api_router.include_router(performance.router)
# api_router.include_router(performance.router,)