from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('home', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logintutor', views.logintutor, name="logintutor"),
    path('loginstudent', views.loginstu, name="loginstu"),
    ]