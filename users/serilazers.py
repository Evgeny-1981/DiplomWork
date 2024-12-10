from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "password",
            "role",
            "image",
            "token",
            "uid",
        )


class PasswordResetRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, data):
        email = data["email"]
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Указанный email не найден."})
        return data


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["password"]
