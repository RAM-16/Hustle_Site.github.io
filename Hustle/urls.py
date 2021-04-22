"""Hustle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Contact import views
from django.contrib.auth import views as uv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homeredirect'),
    path('home', views.home, name='home'),
    path('login/',uv.LoginView.as_view(template_name='Contact/login.html'),name='login'),
    path('logout/',uv.LogoutView.as_view(template_name='Contact/logout.html'),name='logout'),
    path('blog', views.blog, name='blog'),
    path('portal', views.portal, name='portal'),
    path('portfolio', views.portfolio, name='portfolio'),
    # path('register', views.register, name='register'),
]