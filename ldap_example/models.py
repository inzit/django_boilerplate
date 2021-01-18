from django.db import models

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType





# Create your models here.

class ProtectedObject(models.Model):
    ''' This object can only be seen if member of a specific group '''

    class Meta:
        permissions = (
            
        )
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
