from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('moviesingle/', views.moviesingle, name='moviesingle'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]