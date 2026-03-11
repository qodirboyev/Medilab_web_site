
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from formalar.models import Appointment
from home.forms import ADD_user
from hospital.models import Doctor, Department, Service

# Create your views here.
def view_templates(request):
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    services = Service.objects.all()
    appointments = Appointment.objects.all()
    context = {'doctors': doctors,
               'departments': departments,
               'services': services,
               'appointments': appointments,}

    return render(request,'index.html', context)
class SignUpView(CreateView):
    form_class = ADD_user
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')