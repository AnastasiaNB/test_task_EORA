import os
import random
import string
import time

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from pyrogram import Client
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import Message
from schemas import (LoginDataSchema,
                     LoginCodeSchema,
                     LoginByPhoneSchema,
                     MessageSchema,
                     BotAnswerSchema,
                     LoginSuccessSchema)

load_dotenv()

router = APIRouter()

symbols = string.ascii_letters + string.digits
session_name = ''.join(random.choice(symbols) for _ in range(10))
app = Client(
    session_name,
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH')
)


@router.post('/get-login-code', response_model=LoginCodeSchema)
async def get_login_code(
    login_data: LoginDataSchema
):
    login_data = login_data.dict()
    phone_number = login_data['phone_number']
    await app.connect()
    code = await app.send_code(phone_number=phone_number)
    code_hash = code.phone_code_hash
    return {'code_hash': code_hash}


@router.post('/login', response_model=LoginSuccessSchema)
async def login(
    login_by_phone: LoginByPhoneSchema
):
    login_by_phone = login_by_phone.dict()
    phone_number = login_by_phone['phone_number']
    phone_code_hash = login_by_phone['phone_code_hash']
    phone_code = login_by_phone['phone_code']
    user = await app.sign_in(
        phone_number=phone_number,
        phone_code_hash=phone_code_hash,
        phone_code=phone_code
    )
    return {
        'message': f'Login as @{user.username} (user_id - {user.id}) successful'
    }


@router.post('/write-message', response_model=BotAnswerSchema)
async def write_message(
    message_data: MessageSchema,
    session: AsyncSession = Depends(get_async_session)
):
    message_data = message_data.dict()
    user_id = message_data['user_id']
    text = message_data['message']
    message = await app.send_message(
        chat_id='@EoraTaskBot',
        text=text
    )
    stmt = insert(Message).values(
        user_id=user_id,
        message=text
    )
    await session.execute(stmt)
    await session.commit()
    time.sleep(2)
    async for message in app.get_chat_history(chat_id='@EoraTaskBot', limit=1):
        bot_message = message.text
    if bot_message == text:
        return {
            'answer_from_bot': 'Bot has no answer for your message. Please try something else'
        }
    return {'answer_from_bot': bot_message}
