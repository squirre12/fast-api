from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from schema import user_schema
from models.users import User
from security import get_password_hash


def list_users(db: Session, skip: int, limit: int):
    all_user = db.query(User).offset(skip).limit(limit).all()
    return all_user


def user_by_email(db: Session, email: str):
    return db.query(User).filter(User.mail == email).first()


def create(db: Session, data: user_schema.CreateUser):
    db_user = User(username=data.username,
                   first_name=data.first_name,
                   second_name=data.second_name,
                   password=get_password_hash(data.password),
                   mail=data.mail
                   )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(db:Session, data:user_schema.UserBase, update_user: User):
    update_user.first_name = data.first_name
    update_user.second_name = data.second_name
    update_user.username = data.username
    db.commit()
    return update_user


def update_field(db:Session, data:user_schema.UserBase, update_user: User):
    if data.first_name:
        update_user.first_name = data.first_name
    if data.second_name:
        update_user.second_name = data.second_name
    if data.username:
        update_user.username = data.username
    db.commit()
    return update_user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return user