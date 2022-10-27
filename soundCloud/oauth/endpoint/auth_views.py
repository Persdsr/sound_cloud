from django.contrib.auth import logout
from django.shortcuts import render, redirect


def google_login(request):
    """Страница входа через Google"""
    return render(request, 'oauth/google_login.html')

def Logout(request):
    logout(request)
    return redirect('/')