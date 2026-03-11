from django import forms
from .models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Atinizdi kiritin',
                'data-rule': 'minlen:4'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email manziliniz',
                'data-rule': 'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon nomeriniz'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'department': forms.Select(attrs={
                'class': 'form-select'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-select'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
                'placeholder': 'message (optional)'
            }),
        }