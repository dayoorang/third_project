from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profilesapp.forms import ProfileCreationForm
from profilesapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profilesapp/create.html'
    success_url = reverse_lazy('accountsapp:hello_world')