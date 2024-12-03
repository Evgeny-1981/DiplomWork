from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad
from ads.paginators import CustomPagination
from ads.serilazers import AdSerializer
from users.permissions import IsAdmin, IsOwner


class AdCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания объявления."""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Привязка автора объявления к текущему пользователю"""
        ad = serializer.save()
        ad.author = self.request.user
        print(ad.author)
        ad.save()


class AdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка всех объявлений"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        "title",
        "description",
    )
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра объявления"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]


class AdUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения объявления"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsAdmin,
    )


class AdDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления объявления"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsAdmin,
    )


class MyAdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка объявлений пользователя"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     """Список объявленй автора"""
    #     user = self.request.user
    #     queryset = Ad.objects.filter(author=user)
    #     return queryset

    def get_queryset(self):
        """Список объявлений автора"""

        user = self.request.user
        return super().get_queryset().filter(author=user)
