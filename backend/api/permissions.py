from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет доступ только автору объекта,
    администратору или для чтения.
    """

    def has_object_permission(self, request, view, obj):
        is_author = obj.author == request.user
        is_read_only = request.method in permissions.SAFE_METHODS
        is_admin = request.user.is_superuser

        return is_author or is_read_only or is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет доступ только администратору или для чтения.
    """

    def has_permission(self, request, view):
        is_read_only = request.method in permissions.SAFE_METHODS
        is_admin = request.user.is_staff

        return is_read_only or is_admin
