from rest_framework import permissions
import datetime 
from django.utils import timezone
from datetime import timedelta


class IsNotExpired(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):
        if request.method != 'PUT':
            return True
       
        time = obj.avatara.uploaded_at + timedelta(hours=4)
        
        return timezone.now() <= time
    

