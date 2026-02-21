from fastapi import APIRouter
from app.middleware.metrics import get_system_metrics
router=APIRouter()

@router.get("/performance")
def get_metrics():
    return get_system_metrics()
    