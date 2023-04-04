from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwt_manager import create_token
from fastapi import APIRouter

user_router = APIRouter()

#login user
@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(content=token)