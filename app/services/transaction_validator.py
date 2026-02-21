from app.models.models import TransactionValidator, TransactionValidatorResponse


def transaction_validator(obj: TransactionValidator):
    
    seen=set()
    response_model = TransactionValidatorResponse(valid=[], invalid=[])
    for expense in obj.transactions:
        if expense.amount < 0:
            d = expense.model_dump()
            d['message'] = "Negative amounts are not allowed"
            response_model.invalid.append(d)
            continue
        key=tuple(expense.model_dump().items())
        if key in seen:
            d = expense.model_dump()
            d['message'] = "Duplicate Transaction"
            response_model.invalid.append(d)
            continue
        seen.add(key)
        response_model.valid.append(expense)
    return response_model
