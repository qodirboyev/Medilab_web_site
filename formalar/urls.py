from django.urls import path
from .views import make_appointment,contact_view
urlpatterns = [
    path('appointment/',make_appointment,name='appointment_view'),
    path('contact/',contact_view,name='contact_view'),
]