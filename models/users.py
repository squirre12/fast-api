from database.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    second_name = Column(String)
    password = Column(String)
    mail = Column(String, unique=True)
