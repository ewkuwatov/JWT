from fastapi import FastAPI
from passlib.context import CryptContext

from dent_models import LoginModel, RegisterModel, Token
from jwtservice import create_access_token, verify_token

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#############
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
###############

app = FastAPI(docs_url='/')


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = verify_token(token)
    if payload is None:
        raise credentials_exception
    return payload


@app.get('/home')
async def home():
    return {'hello': 'world'}

@app.post('/login')
async def login_user(user: LoginModel):
    result = create_access_token(user.model_dump(), 20)

    return {'jwt': result}

@app.post('/register')
async def register_user(user: RegisterModel):
    pass

@app.get("/secure-data")
async def secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": "This data is secure", "user": current_user}



