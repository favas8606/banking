
from django.urls import path
from . import views

app_name = 'bankapp'
urlpatterns =[
    path('',views.home, name='home'),
    path('form',views.registration_form, name="registration_form"),
    path('services',views.services, name="services"),
    path('transfer',views.transfer, name="transfer"),



]