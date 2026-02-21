from pydantic import BaseModel,field_serializer
from datetime import datetime

class ExpenseModel(BaseModel):
    date: datetime
    amount: float
    # Serialize datetime to your desired string format
    @field_serializer("date")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    

class ExpenseResponse(BaseModel):
    date: datetime
    amount: float
    ceiling: float
    remanent: float
    @field_serializer("date")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")

class TransactionValidator(BaseModel):
    wage: float
    transactions: list[ExpenseResponse]

class TransactionValidatorResponse(BaseModel):
    valid: list[ExpenseResponse]
    invalid: list


class Q(BaseModel):
    fixed: float
    start:datetime
    end: datetime
    @field_serializer("start")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    
    @field_serializer("end")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")

class P(BaseModel):
    extra: float
    start: datetime
    end: datetime
    @field_serializer("start")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    
    @field_serializer("end")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")

class K(BaseModel):
    start: datetime 
    end: datetime
    @field_serializer("start")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    
    @field_serializer("end")
    def serialize_date(self, value: datetime, info):
        return value.strftime("%Y-%m-%d %H:%M:%S") 

class TransactionFilter(BaseModel):
    q: list[Q]
    p:list[P]
    k:list[K]
    wage: float
    transactions: list[ExpenseModel]

class TransactionFilterResponse(BaseModel):
    valid: list
    invalid:list


class ReturnModel(BaseModel):
    age: int
    wage: float
    inflation: float
    q: list[Q]
    p: list[P]
    k: list[K]
    transactions: list[ExpenseModel]