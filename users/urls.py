from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (UserCreateAPIView,)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
                  path('register/', UserCreateAPIView.as_view(), name='user_create'),
                  # path('users/', UserListAPIView.as_view(), name='user_list'),
                  # path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
                  # path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
                  # path('users/delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
                  # path('users/payments/', PaymentListAPIView.as_view(), name='payment_get'),
              ]
