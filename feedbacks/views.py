from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.paginators import CustomPagination
from ads.serilazers import AdDetailSerializer
from feedbacks.models import Feedback
from feedbacks.serilazers import FeedbackSerializer
from users.permissions import IsAdmin, IsOwner


class FeedbackCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Привязываем отзыв к автору и объявлению"""
        feedback = serializer.save()
        feedback.author = self.request.user
        feedback.ad = Ad.objects.get(pk=self.kwargs["pk"])
        print(feedback.ad)
        feedback.save()


class FeedbackListAPIView(generics.ListAPIView):
    """Контроллер для просмотра всех отзывов объявления"""
    serializer_class = AdDetailSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        """Метод для получения отзывов объявления"""
        pk = self.kwargs.get("pk")
        ad = get_object_or_404(Ad, id=pk)
        feedbacks_list = ad.ad_feedback.all()
        return feedbacks_list


class FeedbackRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated,)


class FeedbackUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin,)


class FeedbackDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin,)


class MyFeedbackListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка отзывов пользователя"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
    pagination_class = CustomPagination

    def get_queryset(self):
        """Метод для получения списка отзывов пользователя"""

        author = self.request.user
        return super().get_queryset().filter(author=author)
