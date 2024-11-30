from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Ad(models.Model):
    """Создание модели объявления"""

    title = models.CharField(max_length=255, default='Объявление', verbose_name='Название')
    price = models.PositiveIntegerField(default=100, verbose_name='Стоимость')
    description = models.TextField(default='Описания товара пока нет', verbose_name='Описание')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner',
                               verbose_name='Владелец объявления', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата и время создания объявления', **NULLABLE)

    class Meta:
        db_table = "ads"
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at', 'price',)

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.author}, {self.price}, '
