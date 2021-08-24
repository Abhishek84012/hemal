from django.contrib import admin
from oauth_app.models import Person
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile_number' ,'date_of_birth', 'gender']
