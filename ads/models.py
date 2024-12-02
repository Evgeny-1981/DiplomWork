from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Ad(models.Model):
    """Создание модели объявления"""

    title = models.CharField(max_length=255, verbose_name='Название объявления')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость товара/услуги')
    description = models.TextField(default='Автор пока не создал описания', verbose_name='Описание')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner',
                               verbose_name='Владелец объявления', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления',
                                      **NULLABLE)

    class Meta:
        db_table = "ads"
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.author}, {self.price}, '
