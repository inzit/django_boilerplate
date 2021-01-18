from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from .models import *

import logging
logger = logging.getLogger(__name__)



''' Decorator for checking if a uer is in a group '''
def group_required(*group_names):
    '''Requires user membership in at least one of the groups passed in.'''
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser :
                return True
        return False
    return user_passes_test(in_groups, login_url='access_denied')



'''Using classbased Views:  ONly login required'''
@method_decorator(login_required, name='dispatch')
class ProtectedObjectListView(ListView):
    model = ProtectedObject
    context_object_name = 'protected_object_list'
    template_name='list_view.html'

''' Login, and be a member of "django_staff" or 'django_users' ''' 
@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('django_staff', 'django_users'), name='dispatch')
class ProtectedObjectListViewGroup(ListView):
    model = ProtectedObject
    context_object_name = 'protected_object_list'
    template_name='list_view.html'



'''Using "normal"  views, but only a login is required'''
@login_required
def normalView(request):
    ObList = ProtectedObject.objects.all()
    return render(request, 'list_view.html', {'protected_object_list': ObList})

''' login and check if user is member of 'django_staff' '''
@login_required
@group_required('django_staff')
def normalUserGroup(request):
    ObList = ProtectedObject.objects.all()
    return render(request, 'list_view.html', {'protected_object_list': ObList})
