from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)
