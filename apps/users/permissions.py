from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "doctor"


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "patient"


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
