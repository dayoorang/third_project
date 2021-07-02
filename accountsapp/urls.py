from django.urls import path
from .views import (
     index,
     hello_world
)

app_name = 'accountsapp'

urlpatterns = [
    path('', index, name = 'index'),
    path('hello_world/', hello_world, name = 'helloworld')
]