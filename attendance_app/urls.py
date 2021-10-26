from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in', views.signup, name='sign-in'),
    path('home-page', views.loggedIn, name='home-page'),
]