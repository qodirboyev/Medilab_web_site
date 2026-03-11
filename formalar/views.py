from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact,Appointment
def make_appointment(request):
    if request.method == "POST":
        form = Appointment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_view')
    return redirect('doctor_view')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('doctor_view')
    return redirect('doctor_view')