from rest_framework import serializers
from ads.models import Ad
from feedbacks.models import Feedback


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор модели объявлений"""

    class Meta:
        model = Ad
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели отзыва"""

    class Meta:
        model = Feedback
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного объявления"""
    feedback = FeedbackSerializer(source='feedback_ad', read_only=True, many=True)

    class Meta:
        model = Feedback
        fields = '__all__'
