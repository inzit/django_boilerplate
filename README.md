## Boilerplate for Django, including base template and example for LDAP...

Adding / Removing apps:
Via settings.py or via env_file

## usage: 
copy ois/settings.example.py to settings.py and adjust accordingly
(not required: copy env.example and update, and pass as argument to docker-compose, or add to docker-compose.yml)

    docker-compose up -d
open browser to localhost:8000


### IMPORTANT NOTE!
In the current docker-compose.yml, a static makemigrations for LDAP is defined. Remove that!



## Group permissions automatically:

Example:
## Programmatically add permissions:
```python
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
```
        
## Group permissions decorator:
```python
''' Decorator for checking if a user is in a group '''
def group_required(*group_names):
    '''Requires user membership in at least one of the groups passed in.'''
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser :
                return True
        return False
    return user_passes_test(in_groups, login_url='access_denied')
```
After that, add one more groups to the decorator. See example in views.py
