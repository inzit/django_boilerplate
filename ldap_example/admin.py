from django.contrib import admin
from .models import ProtectedObject
# Register your modelfrom .models import ProtectedObjects here.

@admin.register(ProtectedObject)
class ProtectedObjectAdmin(admin.ModelAdmin):
    pass
