from dataclasses import fields

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ADD_user,Update_user
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = ADD_user
    form = Update_user
    model = CustomUser
    list_display = ('username','email', 'first_name', 'last_name','age','is_staff')
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)