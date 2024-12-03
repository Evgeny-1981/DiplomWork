from rest_framework import serializers

from ads.models import Ad
from feedbacks.serilazers import FeedbackSerializer


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор модели объявлений"""

    class Meta:
        model = Ad
        fields = '__all__'
        search_fields = ("title", "description",)


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного объявления"""
    feedback = FeedbackSerializer(source='feedback_ad', read_only=True, many=True)

    class Meta:
        model = Ad
        fields = '__all__'
