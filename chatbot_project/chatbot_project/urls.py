# chatbot_app/urls.py
from django.urls import path
from chatbot_app.views import home

urlpatterns = [
    path('', home, name='home'),
]
