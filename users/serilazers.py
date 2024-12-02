# добавил01122024
from rest_framework import serializers

from users.models import User
from users.validators import PasswordLengthValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# добавил 01122024
class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, data):
        email = data['email']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Указанный email не найден.'})
        return data


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)
