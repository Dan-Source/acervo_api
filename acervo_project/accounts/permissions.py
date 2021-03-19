from rest_framework.permissions import BasePermission


SAFE_METHOD = ['GET', 'OPTIONS', 'HEAD']


class IsUserOwner(BasePermission):

        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.owner == request.user