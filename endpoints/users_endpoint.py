from typing import Generator, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from database.database import SessionLocal
from schema.user_schema import UserBase, CreateUser, UpdateUser
from utils import user_utils

router = APIRouter()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[UserBase])
def get_all_user(
        db: Session = Depends(get_db),
        skip=0,
        limit=100):
    return user_utils.list_users(
        db=db,
        skip=skip,
        limit=limit
    )


@router.post("/", response_model=UserBase)
def create_user(
        data: CreateUser,
        db: Session = Depends(get_db)
):
    user = user_utils.user_by_email(db=db, email=data.mail)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    return user_utils.create(db, data)


@router.put('/{email}', response_model=UserBase)
def update_user(
        data: UserBase,
        email: EmailStr,
        db: Session = Depends(get_db),
):
    user = user_utils.user_by_email(db=db, email=email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email does not exists in the system.",
        )
    return user_utils.update(db, data, user)


@router.patch('/{email}', response_model=UserBase)
def update_field_user(
        data: UpdateUser,
        email: EmailStr,
        db: Session = Depends(get_db),
):
    user = user_utils.user_by_email(db=db, email=email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email does not exists in the system.",
        )
    return user_utils.update_field(db, data, user)


@router.delete('/{email}', response_model=UserBase)
def delete_user(email: EmailStr, db: Session = Depends(get_db)):
    user = user_utils.user_by_email(db=db, email=email)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email does not exists in the system.",
        )
    return user_utils.delete_user(db, user)