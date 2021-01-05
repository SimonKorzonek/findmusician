from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = "Your account has been created."

class ProfileListView(ListView):
    model = Profile
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = ['profile_pic', 'city', 'kind', 'instruments', 'generes', 'open_for_coop', 'form_of_coop', 'bio']
    success_message = "Your profile has been updated."
