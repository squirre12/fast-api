from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    first_name: str
    second_name: str

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str
    mail: EmailStr

    class Config:
        orm_mode = True


class UpdateUser(UserBase):
    username: Optional[str] = None
    first_name: Optional[str] = None
    second_name: Optional[str] = None

    class Config:
        orm_mode = True