# hello/views.py
from django.http import HttpResponse
from .models import Employee

def hello_world(request):
    return HttpResponse("Hello, World!")

def employee_list(request):
    employees = Employee.objects.all()
    return HttpResponse(employees)
