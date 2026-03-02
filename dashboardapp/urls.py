from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdetails', views.getdetails, name='getdetails'),
    path('authorization_server', views.authorization_server, name = "authorization_server"),
]