from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from ads.models import Ad
from users.models import User


class AdTestCase(APITestCase):
    """Класс для проверки корректности работы CRUD объявлений"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.user.set_password("test")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.ad = Ad.objects.create(
            title="Тестовое объявление №1",
            price=1000,
            description="Тестовое описание об объявлении №1",
            created_at="2024-12-04T15:00:00Z",
            author=self.user,
        )

    def test_create_ad(self):
        """Создание объявления"""
        url = reverse("ads:ad_create")
        data = {
            "title": "Тестовое объявление №2",
            "price": 2000,
            "description": "Тестовое описание об объявлении №2",
            "created_at": "2024-12-04T16:00:00Z",
            "author": self.user.pk,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ad.objects.count(), 2)
        self.assertTrue(Ad.objects.all().exists())

    def test_ads_list(self):
        """Вывод списка объявлений"""
        url = reverse("ads:ad_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.ad.pk,
                    "title": "Тестовое объявление №1",
                    "price": 1000,
                    "description": "Тестовое описание об объявлении №1",
                    "created_at": self.ad.created_at,
                    "author": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(data, result)

    #
    def test_ad_retrieve(self):
        """Проверка корректности данных"""
        url = reverse("ads:ad_retrieve", args=(self.ad.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], self.ad.title)
        self.assertEqual(data["price"], self.ad.price)
        self.assertEqual(data["description"], self.ad.description)
        # self.assertEqual(data["created_at"], self.ad.created_at)
        self.assertEqual(data["author"], self.user.pk)

    def test_ad_update(self):
        """Проверка обновления объявления"""
        url = reverse("ads:ad_update", args=(self.ad.pk,))
        data = {
            "title": "Тестовое объявление №1 обновлено",
            "description": "Тестовое описание об объявлении №1 обновлено",
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], "Тестовое объявление №1 обновлено")
        self.assertEqual(
            data["description"], "Тестовое описание об объявлении №1 обновлено"
        )

    def test_ad_delete(self):
        """Проверка удаления объявления"""
        url = reverse("ads:ad_delete", args=(self.ad.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.count(), 0)
