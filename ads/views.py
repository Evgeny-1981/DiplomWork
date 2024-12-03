from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad
from ads.paginators import CustomPagination
from ads.serilazers import AdDetailSerializer, AdSerializer
from users.permissions import IsAdmin, IsOwner


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
    permission_classes = [AllowAny]
    queryset = Ad.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("title", "description",)
    pagination_class = CustomPagination


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


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
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     """Список объявлений автора"""
    #     user = self.request.user
    #     queryset = Ad.objects.filter(author=user)
    #     return queryset

    def get_queryset(self):
        """Список объявлений автора"""

        user = self.request.user
        return super().get_queryset().filter(author=user)
