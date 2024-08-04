from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),  
    path('success/', views.success, name='success'),
    path('contact_form/', views.contact_form, name='contact_form')
]