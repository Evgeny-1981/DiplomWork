from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad
from feedbacks.models import Feedback
from users.permissions import IsAdmin, IsOwner
from ads.paginators import CustomPagination
from ads.serilazers import AdDetailSerializer, AdSerializer
from feedbacks.serilazers import FeedbackSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания объявления."""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Привязка автора объявления к текущему пользователю"""
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()


class AdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка всех объявлений"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("title", "description",)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated,)


class AdUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения объявления"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin,)


class AdDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления объявления"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin,)


class MyAdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка объявлений пользователя"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_queryset(self):
        """Список объявлений автора"""
        user = self.request.user
        queryset = Ad.objects.filter(author=user)
        return queryset


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
