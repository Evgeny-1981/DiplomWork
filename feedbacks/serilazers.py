from rest_framework import serializers

from feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели отзыва"""

    class Meta:
        model = Feedback
        fields = '__all__'
