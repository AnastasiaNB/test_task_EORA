import random
import string

from fastapi import APIRouter, Depends
from pyrogram import Client
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from schemas import (LoginDataSchema,
                     LoginCodeSchema,
                     LoginByPhoneSchema,
                     MessageSchema)

router = APIRouter()

symbols = string.ascii_letters + string.digits
session_name = ''.join(random.choice(symbols) for _ in range(10))
app = Client(session_name)


@router.post('/get-login-code', response_model=LoginCodeSchema)
async def get_login_code(
    login_data: LoginDataSchema
):
    login_data = login_data.dict()
    api_id = login_data['api_id']
    api_hash = login_data['api_hash']
    phone_number = login_data['phone_number']
    app = Client(
        session_name, api_id=api_id, api_hash=api_hash
    )
    await app.connect()
    code = await app.send_code(phone_number=phone_number)
    code_hash = code.phone_code_hash
    return code_hash


@router.post('/login')
async def login(
    login_by_phone: LoginByPhoneSchema
):
    login_by_phone = login_by_phone.dict()
    phone_number = login_by_phone['phone_number']
    phone_code_hash = login_by_phone['phone_code_hash']
    phone_code = login_by_phone['phone_code']
    a = await app.sign_in(
        phone_number=phone_number,
        phone_code_hash=phone_code_hash,
        phone_code=phone_code
    )
    print(a)
    return 'Login successful'


@router.post('/write-message')
async def write_message(
    message_data: MessageSchema,
    session: AsyncSession = Depends(get_async_session)
):
    message_data = message_data.dict()
    user_id = message_data['user_id']
    message = message_data['message']
    x = await app.send_message(
        chat_id='@EoraTaskBot',
        text=message
    )
    print(x)
    return 11111

