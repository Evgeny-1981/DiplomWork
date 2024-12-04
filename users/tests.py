from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestRegisterUser(APITestCase):
    """Проверка регистрации пользователя"""

    def test_successful_user_registration(self):
        url = reverse("users:register")
        data = {
            "email": "test@test.ru",
            "password": "test",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
