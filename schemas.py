from pydantic import BaseModel
from datetime import date
from enum import Enum

class TransactionStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    open_status = "open"

class TransactionBase(BaseModel):
    employee_name: str
    department: str
    director: str
    transaction_date: date
    transaction_status: TransactionStatus
    location: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
