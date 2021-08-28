from django.contrib import admin
from employee_management.models import Employee
# Register your models here.

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['id', 'employee_name',
                    'employee_phone', 'employee_department', 'employee_gender']
