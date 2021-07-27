from django.contrib import admin
from django.urls import path, include

from profilesapp.views import ProfileCreationView

app_name ='profileapp'
urlpatterns = [

    path('create/',ProfileCreationView.as_view(), name = 'create' )

]