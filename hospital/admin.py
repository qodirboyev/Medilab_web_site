from django.contrib import admin
from .models import Doctor, Department, Service

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Service)