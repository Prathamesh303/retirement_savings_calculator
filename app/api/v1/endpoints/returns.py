from fastapi import APIRouter
from app.models.models import ReturnModel
from app.services.calculate_returns import returns
router=APIRouter()

@router.post("/returns:nps")
def return_nps(obj: ReturnModel):
    return returns(obj)
    pass

@router.post("/returns:index")
def return_index(obj: ReturnModel):
    return returns(obj, calc="index")
    pass