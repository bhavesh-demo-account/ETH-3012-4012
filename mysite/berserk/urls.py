from django.urls import path, include
from . import views

urlpatterns = [
    path('navigation/', views.navigation, name='navigation'),
    path('register/', views.registration, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.login, name='login'),
]