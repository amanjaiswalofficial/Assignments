from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class DidOwnerCreateQuestion(permissions.BasePermission):

    def __init__(self, request):
        self.request = request

    def has_object_permission(self, request, view, obj):
        #print('inside create user permission')
        res = Questions.objects.get(id = int(self.request.POST['question']))
        return res.owner_id == request.user.id