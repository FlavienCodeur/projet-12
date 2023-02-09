from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from .models import Events

class SupportPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'POST':
            if request.user.assignment.department == 'Support':
                return False
            return True
        elif request.user.assignment.department == 'Sales':
            return False

        return True

    def has_object_permission(self, request, view, obj):

        if obj[0].support_contact == request.user:
            return True

        return False

         


