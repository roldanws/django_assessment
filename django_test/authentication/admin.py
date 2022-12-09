from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

#@admin.register(get_user_model())
@admin.register(CustomUser)
#class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password','rol')


admin.site.unregister(Group)
