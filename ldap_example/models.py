from django.db import models




# Create your models here.

class ProtectedObject(models.Model):
    ''' This object can only be seen if member of a specific group '''

    class Meta:
        app_label = 'ldap_example'

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
