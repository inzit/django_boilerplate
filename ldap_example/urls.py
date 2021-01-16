from django.urls import path
from . import views


app_name = 'ldap-example'

urlpatterns = [
    path('cbv', views.ProtectedObjectListView.as_view()),
    path('cbv_group', views.ProtectedObjectListViewGroup.as_view()),

    path('normal', views.normalView),
    path('normal_group', views.normalUserGroup),

    
]
