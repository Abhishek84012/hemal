from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from views_type_app.models import Employee
from views_type_app.forms import EmployeeForm


class EmployeeListView(ListView):
    template_name = "employee_list_view.html"
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee_create_view.html"
    fields = ['employee_name','employee_phone', 'employee_department', 'employee_gender']
    success_url = "/"


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee_update_view.html"
    fields = ['employee_name','employee_phone', 'employee_department', 'employee_gender']
    success_url = "/"

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = "ListView"
    template_name = "employee_delete_view.html"
    success_url = "/"

# class EmployeeDetailsV