from django.db import models
class Employee(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('OTHER', 'not specified'),
    )
    employee_name = models.CharField(max_length=10)
    employee_phone = models.CharField(max_length=10)
    employee_department = models.CharField(max_length=10)
    employee_gender = models.CharField(choices=GENDER_CHOICES , max_length=10)
