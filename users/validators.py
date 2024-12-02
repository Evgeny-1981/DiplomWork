from django.core.exceptions import ValidationError


class PasswordLengthValidator:
    def __call__(self, value):
        if len(value) < 8:
            raise ValidationError({'password': 'Пароль должен быть не менее 8 символов.'})
