from app.models.models import TransactionFilter, TransactionValidator,Q,P,ExpenseResponse,TransactionFilterResponse
from app.services.expense_parse import expense_parse
from app.services.transaction_validator import transaction_validator
from datetime import datetime

def filter_based_on_q(valid_transactions:list[ExpenseResponse],list_of_q: list[Q]):
    dict_ = {}
    for obj in valid_transactions:
        list_ = []
        for q_obj in list_of_q:
            if q_obj.start <= obj.date <= q_obj.end:
                list_.append((q_obj.start,q_obj.fixed))
        if list_:
            fixed_value = min(list_, key=lambda t: abs(t[0] - obj.date))[1]
            dict_[obj.date]= fixed_value
    return dict_

def filter_based_on_p(valid_transactions:list[ExpenseResponse], list_of_p:list[P]):
    dict_ = {}
    for obj in valid_transactions:
        extra=0
        for p_obj in list_of_p:
            if p_obj.start <= obj.date <= p_obj.end:
                extra+=p_obj.extra
        if extra !=0:
            dict_[obj.date] = extra
    return dict_
    pass

def transaction_filter(obj: TransactionFilter):
    response_list = expense_parse(obj.transactions)
    validator_ = transaction_validator(
        TransactionValidator(wage=obj.wage,
                             transactions=response_list))
    q_dict = filter_based_on_q(validator_.valid, obj.q)
    p_dict = filter_based_on_p(validator_.valid, obj.p)
    valid_list=[]
    for obj_ in validator_.valid:
        if obj_.date in q_dict:
            obj_.remanent = q_dict[obj_.date]
        
        if obj_.date in p_dict:
            obj_.remanent += p_dict[obj_.date]
        d_=obj_.model_dump()
        d_["inkPeriod"] = True
        valid_list.append(d_)
    return TransactionFilterResponse(valid=valid_list,invalid=validator_.invalid)