# chatbot_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

MODE_URI = os.getenv('MODE_URI')
API_KEY = os.getenv('API_KEY')


def home(request):
    bot_response = None  # Инициализируем переменную для ответа от бота

    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        prompt = {
            "modelUri": MODE_URI,
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Ты помогаешь в разборе юридических документов."
                },
                {
                    "role": "user",
                    "text": user_message
                }
            ]
        }

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {API_KEY}"
        }

        response = requests.post(url, headers=headers, json=prompt)
        
        try:
            result = response.json()
            bot_response = result.get('result', {}).get('alternatives', [{}])[0].get('message', {}).get('text')
        except json.JSONDecodeError:
            bot_response = 'Invalid JSON response from API'

    return render(request, 'home.html', {'bot_response': bot_response})
