# chatbot_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    if request.method == 'POST':
        prompt = {
            "modelUri": "gpt://<b1gevpns458a0bh39eo3>/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": "Ты ассистент дроид, способный помочь в галактических приключениях."
                },
                {
                    "role": "user",
                    "text": request.POST.get('user_message')  # Получаем сообщение от пользователя из POST-запроса
                }
            ]
        }

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Api-Key <AQVN0pevSYxOLiNpGizMmjdp0fzM9UCjSaKubhRm>"
        }

        response = requests.post(url, headers=headers, json=prompt)
        result = response.json()

        bot_response = result['replies'][0]['text']  # Получаем ответ от бота

        return JsonResponse({'bot_response': bot_response})
    
    return render(request, 'home.html')
