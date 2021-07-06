from django.urls import path
from .views import (
     hello_world
)

app_name = 'accountsapp'

urlpatterns = [
    path('hello_world/',hello_world, name ='hello_world')
]