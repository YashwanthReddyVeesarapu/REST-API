from datetime import datetime, timedelta
from typing import Union
from fastapi import APIRouter, HTTPException
from jose import JWTError, jwt

from .. import models

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


preusername = "red"
prepassword= "#1#23#4#"

router = APIRouter(prefix="/redflix", tags=['Redflix'])

SECRET_KEY = "09d25e-094f-"+ str(datetime.utcnow().date()) + "aa-6ca2-556" + str(datetime.utcnow().hour)
print(SECRET_KEY)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username):
    if preusername == username:
        return True
    else:
        return False

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta,None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post('/login')
def login(data: models.Redflixlogin):
    if preusername == data.username and prepassword == data.password:
        return {"msg": "success", "accessToken": SECRET_KEY}
    else:
        raise HTTPException(status_code=404, detail="Not Found")

@router.post('/verify-access-token')
def verify_login(data: models.LoginToken):
    if data.access_token == SECRET_KEY:
        return "success"
    else:
        raise HTTPException(status_code=404, detail="Not Found")
