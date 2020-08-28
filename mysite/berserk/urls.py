from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.registration, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.login_user, name='login'),

]