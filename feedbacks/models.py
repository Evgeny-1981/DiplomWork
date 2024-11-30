from django.db import models
from django.utils import timezone

from ads.models import Ad
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Feedback(models.Model):
    """Создание модели отзыва"""

    text = models.TextField(max_length=400, verbose_name='текст отзыва', )
    author = models.ForeignKey(User, related_name='user_feedback', on_delete=models.CASCADE,
                               verbose_name='Пользователь, оставивший отзыв', **NULLABLE)
    ad = models.ForeignKey(Ad, related_name='ad_feedback', on_delete=models.CASCADE,
                           verbose_name='Объявление, под которым оставлен отзыв', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата и время отзыва', **NULLABLE)

    def __str__(self):
        return f'Отзыв об {self.ad} от {self.author} опубликован {self.created_at}'

    class Meta:
        db_table = "feedbacks"
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('author', 'created_at',)
