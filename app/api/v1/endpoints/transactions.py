from fastapi import APIRouter
from app.models.models import ExpenseModel, TransactionValidator, TransactionFilter
from app.services.expense_parse import expense_parse
from app.services.transaction_validator import transaction_validator
from app.services.transaction_filter import transaction_filter

router=APIRouter()

@router.post("/transaction:parse")
async def transaction_parse(expense_list:list[ExpenseModel]):
    return expense_parse(expense_list)

@router.post("/transaction:validator")
async def transaction_validate(obj: TransactionValidator):
    return transaction_validator(obj)
    pass

@router.post("/transaction:filter")
async def transaction_filtered(obj: TransactionFilter):
    return transaction_filter(obj)
    pass