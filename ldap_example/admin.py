from django.contrib import admin
import logging
from .models import ProtectedObject
# Register your modelfrom .models import ProtectedObjects here.

@admin.register(ProtectedObject)
class ProtectedObjectAdmin(admin.ModelAdmin):
    pass

logger = logging.getLogger(__name__)




## Programmatically add permissions:
from django.contrib.auth.models import Group, Permission

''' define a variable to contain the group, and get the group name. In this case 'django_security_group' '''
try:
    security_group, created = Group.objects.get_or_create(name='django_security_team')


    ''' For a single permission, get the correct permission by name. 
        Check as admin in the admin console what the name exactly is, in this case 'Can view protected object' 
        structure is: Can <ACTION> <Object Name>",  where ACTION is one of "view", "update", "create", "delete"
    '''
    #pm = Permission.objects.get(name='Can view protected object')
    #security_group.permissions.add(pm)

    ''' To get all permissions for a specific object use the filter with the objects name: 
        In this case: "protected object" .. Then loop through the result to add all permissions.
    '''
    all_permissions = Permission.objects.filter(name__contains='protected object')
    for permission in all_permissions:
        security_group.permissions.add(permission)
except Exception as e:
    logger.error("Could not set permissions. %s : %s", e.__str__(), __file__)
