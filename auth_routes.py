from fastapi import APIRouter, status
from database import Session, engine

from schemas import SignUpModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_router = APIRouter()

session = Session(bind=engine)

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@auth_router.get('/')
async def hello():
    return {"message": "Hello world"}

# @auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
# async def signup(user: SignUpModel, session: AsyncSession):
#     # Проверяем, существует ли пользователь с таким email
#     result = await session.execute(select(User).filter(user.email == User.email))
#     db_email = result.scalar_one_or_none()
#
#     if db_email is not None:
#         return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                              detail="User with the email already exists")
#
#     db_email = session.query(User).filter(User.email == user.email).first()
#
#     if db_email is not None:
#         return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                              detail="User with the email already exists")
#     new_user = User(username=user.username, is_active=user.is_active, email=user.email,
#                     is_staff = user.is_staff,
#                     password=generate_password_hash(user.password))
#     session.add(new_user)
#     session.commit()
#     return {"message": "User signed up successfully"}