from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from authentication.admin import UserAdminCreationForm 
from .forms import UserAdminCreationForm, Login



class RegisterView(generic.CreateView):
    form_class = UserAdminCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
