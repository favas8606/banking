from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('registration/', views.register, name="registration"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name ="logout")
]