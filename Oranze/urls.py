"""Oranze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('srch', views.search),    
    path('login', views.login),
    path('adminlogin', views.adminlogin),
    path('admindetails', views.admindetails),
    path('adminsignup', views.adminsignup),
    path('signupadmin', views.signupadmin),            
    path('signup', views.signup),         
    path('booking', views.booking),
    path('show', views.show),
    path('players', views.players),                
    path('entry', views.entry),
    path('adminentry', views.adminentry),
    path('create', views.create),
    path('', views.show),    
    path('edit/<int:game_id>', views.edit),
    path('update/<int:game_id>', views.update),
    path('delete/<int:game_id>', views.delete),   
]
