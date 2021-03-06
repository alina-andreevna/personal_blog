"""my_site URL Configuration

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

from web import views

urlpatterns = [
    path('', views.index),
    path('status', views.status),
    path('contact/', views.contact),
    path('publication/<int:pub_id>', views.publication),
    path('publications/', views.publications),
    path('post/', views.post),
    path('page404/', views.page404),
    path('resume_rus/', views.resume_rus),
    path('resume_eng/', views.resume_eng),
]
