from rest_framework.permissions import BasePermission
import datetime

class IsAuthor(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False
class Future(BasePermission):

    def has_object_permission(self,request,view,obj):
        set = (obj.date - datetime.date.today()).days
        if  set > 3 :
            return True
        else:
            return False
