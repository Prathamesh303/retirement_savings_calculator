import math
from app.models.models import ExpenseModel, ExpenseResponse

def ceil_number(number):
    return math.ceil(number/100)*100

def expense_parse(expense_list:list[ExpenseModel]):
    response_list = []
    for expense in expense_list:
        ceiling = ceil_number(expense.amount)
        remanent = ceiling - expense.amount
        obj = ExpenseResponse(date=expense.date,amount=expense.amount,
                              ceiling=ceiling,remanent=remanent)
        response_list.append(obj)
    return response_list