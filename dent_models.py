from pydantic import BaseModel

class LoginModel(BaseModel):
    username: str
    password: str


class RegisterModel(BaseModel):
    username: str
    password: str
    mail: str

class Token(BaseModel):
    access_token: str
    token_type: str