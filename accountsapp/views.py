from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountsapp.forms import AccountCreationForm
from accountsapp.models import NewModel
from articleapp.models import Article


def hello_world(request):
    if request.user.is_authenticated: # @login rquired 로 대체 가능.
        if request.method == "POST":
            temp = request.POST.get('input_text')

            new_model = NewModel()
            new_model.text = temp
            new_model.save()

            data_list = NewModel.objects.all()

            return HttpResponseRedirect(reverse('accountsapp:hello_world'))
        else:
            data_list = NewModel.objects.all()

            return render(request, 'accountsapp/hello_world.html',
                          context={'data_list': data_list})
    else:
        return redirect('accountsapp:login')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'accountsapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    # success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'accountsapp/update.html'

    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(self,request,*args, **kwargs)
        else:
            return  HttpResponseForbidden()


    def post(self,request,*args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(self,request,*args, **kwargs)
        else:
            return  HttpResponseForbidden()

    def get_success_url(self):
        return reverse('accountsapp:detail', kwargs={'pk':self.object.pk})


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountsapp:hello_world')
    template_name = 'accountsapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()