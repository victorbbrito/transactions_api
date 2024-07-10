from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class TransactionStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, index=True)
    department = Column(String, index=True)
    director = Column(String, index=True)
    transaction_date = Column(Date)
    transaction_status = Column(Enum(TransactionStatus))
    location = Column(String, index=True)
