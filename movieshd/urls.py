"""newott URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from movieshd import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path("login_page",views.login_page, name='login_page'),
    path("logoutuser",views.logoutuser,name='logout_user'),
    path("register_page",views.register_page,name='register_page'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('telugu/',views.telugumovie,name='telugu'),
    path('hindi/',views.hindimovie,name='hindi'),
    path('tamil/',views.tamilmovie,name='tamil'),
    path('malayalam/',views.malayalammovie,name='malayalam'),
    path('english/',views.englishmovie,name='english'),
    path('action/',views.actionmovie,name='action'),
    path('drama/',views.dramamovie,name='drama'),
    path('thriller/',views.thrillermovie,name='thriller'),
    path('allmovies',views.movies,name='allmovies'),
    path('detail/<int:id>',views.moviedetail, name='moviedetail'),
    path('subscription',views.subscription, name='subscription'),
    path('paymentgate',views.paymentgate, name='paymentgate'),

]
