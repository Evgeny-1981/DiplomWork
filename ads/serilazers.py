from rest_framework import serializers

from ads.models import Ad
from feedbacks.models import Feedback
from feedbacks.serilazers import FeedbackSerializer


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор модели объявлений"""

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного объявления"""
    feedback = FeedbackSerializer(source='ad_feedback', read_only=True, many=True)

    class Meta:
        model = Feedback
        fields = '__all__'
