# hello/urls.py
from django.urls import path
from .views import employee_list, hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('employees/', employee_list, name='employee_list'),
]
