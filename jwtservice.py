from jose import JWTError, jwt
from datetime import datetime, timedelta

from config import SECRET_KEY, ALGORITHM

def create_access_token(data: dict, expires_minutes: int):
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    data.update({"exp": expire})
    encode_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return encode_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
        return payload
    except JWTError:
        return None