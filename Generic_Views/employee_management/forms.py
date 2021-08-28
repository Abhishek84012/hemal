from django import forms
from views_type_app.models import Employee

class EmployeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_phone',
                'employee_department', 'employee_gender']
