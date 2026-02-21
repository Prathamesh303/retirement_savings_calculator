from fastapi import APIRouter

router=APIRouter()

@router.get("/performance")
def get_metrics():
    pass