from django.shortcuts import render
from django.views import generic
from employee_management.models import Employee
from django.urls import reverse_lazy


class EmployeeListView(generic.ListView):
    template_name = "employee_list_view.html"
    model = Employee


class EmployeeCreateView(generic.CreateView):
    model = Employee
    template_name = "employee_create_view.html"
    fields = ['employee_name','employee_phone', 'employee_department', 'employee_gender']
    success_url = reverse_lazy('employee_details')
    
class EmployeeUpdateView(generic.UpdateView):
    model = Employee
    template_name = "employee_update_view.html"
    fields = ['employee_name','employee_phone', 'employee_department', 'employee_gender']
    success_url = reverse_lazy('employee_details')

class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    template_name = "employee_delete_view.html"
    success_url = reverse_lazy('employee_details')

# class EmployeeDetailsV
