from django.db import models


class Message(models.Model):
    user_id = models.CharField(max_length=9)
    message = models.TextField(max_length=500)
