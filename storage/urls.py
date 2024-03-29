from django.urls import path
from . import views

urlpatterns = [
    path('', views.storages, name = 'storages'),
    path('/storage/', views.storage, name='storage'), 
    
]