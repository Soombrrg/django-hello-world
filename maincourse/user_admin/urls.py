# user_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about/', views.about, name='about'),
]