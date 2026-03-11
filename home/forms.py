from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ADD_user(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "age")

class Update_user(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "age")
