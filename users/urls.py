from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.apps import UsersConfig
from users.views import CustomTokenObtainPairView, PasswordResetView, ResetPassword
from users.views import UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path(
        "register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "login/",
        CustomTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path(
        "token/verify/",
        TokenVerifyView.as_view(permission_classes=(AllowAny,)),
        name="token_verify",
    ),
    path('reset_password/', PasswordResetView.as_view()),
    path('reset_password_confirm/<str:uid>/<str:token>/', ResetPassword.as_view()),
]
