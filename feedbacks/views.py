from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad
from feedbacks.models import Feedback
from users.permissions import IsAdmin, IsOwner
from ads.paginators import CustomPagination
from ads.serilazers import AdDetailSerializer, AdSerializer
from feedbacks.serilazers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        """Привязываем отзыв к автору и объявлению"""
        feedback = serializer.save()
        feedback.author = self.request.user
        feedback.ad = Ad.objects.get(pk=self.kwargs["ad_pk"])
        feedback.save()

    def get_queryset(self):
        """Метод для получения отзывов объявления"""
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_pk)
        feedback_list = ad.feedback_ad.all()
        return feedback_list

    def get_permissions(self):
        """Прописываем права на коментарии"""

        if self.action in ["create", "list", "retrieve"]:
            permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)
        for permission in permission_classes:
            return permission()
