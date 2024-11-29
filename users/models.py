from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Создание модели пользователя"""

    ROLE_CHOICES = (
        ("user", "user"),
        ("admin", "admin"),
    )
    username = None
    first_name = models.CharField(
        max_length=100, verbose_name="Имя пользователя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=150, verbose_name="Фамилия пользователя", **NULLABLE
    )
    phone = models.CharField(max_length=30, verbose_name="Номер телефона", **NULLABLE)
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="user",
        verbose_name="Роль пользователя",
    )
    image = models.ImageField(upload_to="users/", verbose_name="Аватар", **NULLABLE)
    token = models.CharField(max_length=255, verbose_name="token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, {self.role}"

    class Meta:
        db_table = "users"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ("email", "role", )
