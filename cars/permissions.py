from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #read only
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #write only for author
        return obj.owner == request.user
