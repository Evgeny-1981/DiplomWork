from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
# from views import TokenObtainPairView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, TokenObtainPairView

app_name = UsersConfig.name

# router = DefaultRouter()

urlpatterns = [
    path(
        "register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
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
    )
]
