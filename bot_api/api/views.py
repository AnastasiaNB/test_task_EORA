import os

import requests
from dotenv import load_dotenv
from rest_framework.views import APIView
from telegram import Telegram

from api.serializers import MessageSerializer

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
SEND_MESSAGE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


class AskBotView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tg = Telegram(
            api_id=os.getenv('API_ID'),
            api_hash=os.getenv('API_HASH'),
            phone=os.getenv('PHONE'),
            database_encryption_key='changeme1234',
        )
        tg.login()
        result = tg.get_chats()
        result.wait()
        result = tg.send_message(
            chat_id=318345947,
            text='dfnnvjfkdvn jkxs',
        )
        result.wait()
        tg.stop()
