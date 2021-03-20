from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsUserOwner(BasePermission):

        def has_object_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                if request.user.is_auhenticated:
                    return True
            #return obj.owner == request.user
