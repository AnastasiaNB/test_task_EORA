from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import AskBotView


router = SimpleRouter()

urlpatterns = [
    path('ask-bot/', AskBotView.as_view())
]
