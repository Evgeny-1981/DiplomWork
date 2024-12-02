from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from ads.apps import AdsConfig
from ads.views import AdCreateAPIView, AdListAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, \
    MyAdListAPIView

app_name = AdsConfig.name

router = DefaultRouter()
# router.register(r'(?P<ad_pk>\d+)/comments', CommentViewSet, basename='feedback')

urlpatterns = [
                  path('list/', AdListAPIView.as_view(), name='ad_list'),
                  path('create/', AdCreateAPIView.as_view(), name='ad_create'),
                  path('my_ads/', MyAdListAPIView.as_view(), name='ad_mylist'),
                  path('<int:pk>/', AdRetrieveAPIView.as_view(), name='ad_get'),
                  path('<int:pk>/update/', AdUpdateAPIView.as_view(), name='ad_update'),
                  path('<int:pk>/delete/', AdDestroyAPIView.as_view(), name='ad_delete'),
              ] + router.urls
