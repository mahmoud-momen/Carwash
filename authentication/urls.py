from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('SIGNUP', views.SIGNUP, name='SIGNUP'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('reservation_create', views.reservation_create, name='reservation_create'),
    path('reservation_view/', views.reservation_view, name='reservation_view'),

]