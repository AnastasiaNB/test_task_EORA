from rest_framework.views import APIView
import requests

from api.serializers import MessageSerializer
from bot_api.main import BOT_TOKEN

SEND_MESSAGE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/messages.sendMessage'


class AskBotView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = requests.post(SEND_MESSAGE_URL, data=serializer.data)
