from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.paginators import CustomPagination
from feedbacks.models import Feedback
from feedbacks.serilazers import FeedbackSerializer
from users.permissions import IsAdmin, IsOwner


class FeedbackCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Привязываем отзыв к автору и объявлению"""
        feedback = serializer.save()
        feedback.author = self.request.user
        print(feedback.ad)
        feedback.save()


class FeedbackListAPIView(generics.ListAPIView):
    """Контроллер для просмотра всех отзывов"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     """Метод для получения отзывов объявления"""
    #     pass


class FeedbackRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного отзыва"""
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin,)


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
