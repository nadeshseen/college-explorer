from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('research', views.research, name='research'),
    path('contact', views.contact, name='contact')
]