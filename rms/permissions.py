from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class isAdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.IsAdmin())
