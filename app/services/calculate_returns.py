
from app.models.models import ReturnModel,TransactionFilter
from app.services.transaction_filter import transaction_filter
from datetime import datetime

def calculate_tax(annual_income):
    if annual_income < 700000:
        return 0
    elif annual_income>700000 and annual_income< 1000000:
        return (annual_income-700000)*0.1
    elif annual_income>1000000 and annual_income< 1200000:
        return (annual_income-1000000)*0.15
    elif annual_income>1200000 and annual_income< 1500000:
        return (annual_income-1200000)*0.2
    else:
        return (annual_income-1500000)*0.3
    
def calculate_nps(amount, age, wage, inflation):
    nps=amount*((1+0.0711)**(60-age))
    print(nps)
    nps_deduction=min(amount, 0.1*wage*12, 200000)
    tax_benefit = calculate_tax(wage*12)-calculate_tax(wage*12-nps_deduction)
    
    new_nps = nps/((1+(inflation/100))**(60-age))
    return new_nps, tax_benefit

def calculate_index(amount, age, wage, inflation):
    index_ = amount*(1+0.1449)**(60-age)
    new_index = index_/((1+(inflation/100))**(60-age))
    return new_index

def returns(obj: ReturnModel, calc="nps"):
    #tax_ = calculate_tax(obj.wage*12)
    obj_ =transaction_filter(
        TransactionFilter(q=obj.q,p=obj.p,k=obj.k,
                        wage=obj.wage, 
                        transactions=obj.transactions))
    total_amount = 0
    total_ceiling = 0
    k_dict= {}
    for row in obj_.valid:
        total_amount +=row["amount"]
        total_ceiling += row["ceiling"]

        for k_obj in obj.k:
            if k_obj.start <= datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S") <= k_obj.end:
                if (k_obj.start, k_obj.end) not in k_dict:
                    k_dict[(k_obj.start, k_obj.end)] =0
                k_dict[(k_obj.start, k_obj.end)]+=row["remanent"]
    list_ =[]
    for key in k_dict:
        if calc == "nps":
            calc_return, tax_benefit = calculate_nps(k_dict[key], obj.age, 
                                            obj.wage, obj.inflation)
        else:
            tax_benefit=0
            calc_return= calculate_index(k_dict[key], obj.age, 
                                            obj.wage, obj.inflation)
        d_ = {}
        d_["start"]=key[0].strftime("%Y-%m-%d %H:%M:%S")
        d_["end"]=key[1].strftime("%Y-%m-%d %H:%M:%S")
        d_["amount"]=k_dict[key]
        d_["profit"]=calc_return-k_dict[key]
        d_["taxBenefit"]=tax_benefit
        list_.append(d_)
    
    return {"totalTransactionAmount": total_amount,
            "totalCeiling": total_ceiling,
            "savingsByDates":list_}
    pass 
