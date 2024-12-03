from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from feedbacks.models import Feedback
from feedbacks.serilazers import FeedbackSerializer
from users.permissions import IsAdmin, IsOwner


class FeedbackViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

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

    # def get_permissions(self):
    #     """Прописываем права на комментарии"""
    #
    #     if self.action in ["create", "list", "retrieve"]:
    #         permission_classes = (IsAuthenticated,)
    #     elif self.action in ["update", "partial_update", "destroy"]:
    #         permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)
    #     for permission in permission_classes:
    #         return permission()

    def get_permissions(self):
        """
        Метод для проверки доступа к правам на комментарии в зависимости от роли Пользователя.
        """
        if self.action in ["create", "retrieve", "list"]:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["partial_update", "update", "destroy"]:
            self.permission_classes = (IsAuthenticated, IsAdmin | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsAdmin,)

        return super().get_permissions()
