# добавил011202024
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from config.settings import EMAIL_HOST_USER
from users.models import User
from users.serilazers import UserSerializer, PasswordResetSerializer, ResetPasswordSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Класс для создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response('Неверные учетные данные, повторите попытку')


# добавил01122024
class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']

            user = get_user_model().objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.email))
            token = PasswordResetTokenGenerator().make_token(user)
            user.token = token
            user.uid = uid
            user.save()
            url = get_current_site(request)
            # Создаем ссылку для сброса пароля
            # url = "http://{}/{}/{}/".format(host, uid, token)
            # Отправляем письмо со ссылкой для сброса пароля
            send_mail(
                subject="Запрос сброса пароля с сайта {}".format(url),
                message="Для сброса пароля перейдите по ссылке: http://{}/{}/{}/".format(url, uid, token),
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            return Response("Ссылка для сброса пароля отправлена на вашу электронную почту.")

        else:
            return Response("Введен неверный адрес электронной почты, повторите попытку.")


class ResetPassword(generics.GenericAPIView):
    """Меняем пароль пользователю"""

    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data['token']
        reset_obj = User.objects.filter(token=token).first()
        if not reset_obj:
            return Response('Неверный токен', status=400)
        uid = request.data['uid']
        user = User.objects.filter(uid=uid).first()
        if user:
            new_password = request.data['new_password']
            user.set_password(new_password)
            user.save()
            return Response('Пароль успешно обновлен')
        else:
            return Response('Пользователь не найден')
