from pydantic import BaseModel


class LoginDataSchema(BaseModel):
    api_id: str
    api_hash: str
    phone_number: str


class LoginCodeSchema(BaseModel):
    message: str = 'Login code was sent. Check your Telegram account.'
    code_hash: str


class LoginByPhoneSchema(BaseModel):
    phone_number: str
    phone_code_hash: str
    phone_code: str


class MessageSchema(BaseModel):
    user_id: int
    message: str
