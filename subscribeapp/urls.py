
from django.urls import path, include

from subscribeapp.views import SubscriptionView, SubscriptionListview

app_name = 'subscribeapp'
urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListview.as_view(), name='list'),

]