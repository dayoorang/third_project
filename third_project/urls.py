
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articleapp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountsapp.urls')),
    path('profiles/', include('profilesapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('like/', include('likeapp.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
