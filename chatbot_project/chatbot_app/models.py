# chatbot_app/models.py
from django.db import models

class Conversation(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
