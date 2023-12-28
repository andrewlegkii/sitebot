# chatbot_app/tests.py
from django.test import TestCase
from django.urls import reverse

class ChatbotTest(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
