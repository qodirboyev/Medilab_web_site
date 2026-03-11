from django.urls import path
from .views import view_templates,SignUpView

urlpatterns = [
    path('',view_templates, name='home'),
    path('signup/',SignUpView.as_view(),name='signup'),
]