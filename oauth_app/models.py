from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
# from geography.models import ZipCode

class Person(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile_number = PhoneNumberField()
    date_of_birth = models.DateField()
    # zip_code = ZipCode()
    gender = models.CharField(choices=GENDER,max_length = 6)
    
    
