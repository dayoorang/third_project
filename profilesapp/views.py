from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profilesapp.forms import ProfileCreationForm
from profilesapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profilesapp/create.html'
    success_url = reverse_lazy('accountsapp:hello_world')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'profilesapp/update.html'
