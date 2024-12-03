from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ads.apps import AdsConfig
from ads.views import (
    AdCreateAPIView,
    AdListAPIView,
    AdRetrieveAPIView,
    AdUpdateAPIView,
    AdDestroyAPIView,
    MyAdListAPIView,
)

app_name = AdsConfig.name

router = DefaultRouter()

urlpatterns = [
    path("<int:pk>/feedbacks/", include("feedbacks.urls", namespace="feedbacks")),
    path("list/", AdListAPIView.as_view(), name="ad_list"),
    path("create/", AdCreateAPIView.as_view(), name="ad_create"),
    path("my_list_ads/", MyAdListAPIView.as_view(), name="ad_mylist"),
    path("<int:pk>/", AdRetrieveAPIView.as_view(), name="ad_get"),
    path("<int:pk>/update/", AdUpdateAPIView.as_view(), name="ad_update"),
    path("<int:pk>/delete/", AdDestroyAPIView.as_view(), name="ad_delete"),
] + router.urls
