from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Проверка на администратора"""

    def has_permission(self, request, view):
        return request.user.role == "admin"


class IsOwner(BasePermission):
    """Проверка на владельца объекта"""

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
