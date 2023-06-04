from pydantic import BaseModel


class LoginDataSchema(BaseModel):
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


class BotAnswerSchema(BaseModel):
    answer_from_bot: str = 'Answer from @EoraTaskBot'


class LoginSuccessSchema(BaseModel):
    message: str = 'Login as @username (user_id - id) successful'
