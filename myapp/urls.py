from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_location/', views.get_location, name='get_location'),
]
