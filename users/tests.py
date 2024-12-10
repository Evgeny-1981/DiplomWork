from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestRegisterUser(APITestCase):
    """Проверка регистрации пользователя"""

    def test_successful_user_registration(self):
        url = reverse("users:register")
        data = {
            "email": "test@test.ru",
            "password": "test1238",
        }
        response = self.client.post(url, data, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["email"], "test@test.ru")
        self.assertEqual(data["role"], "user")
        self.assertEqual(data["uid"], None)
        self.assertEqual(data["token"], None)
