from django.contrib.auth import logout
from django.urls import path, include

from django.conf import settings
from .endpoint import auth_views

urlpatterns = [
    path('accounts/login/', auth_views.google_login, name='login'),
    path('accounts/', include('allauth.urls')),
]
