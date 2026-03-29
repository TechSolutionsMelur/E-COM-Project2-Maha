from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('form/',form,name='form'),
    path('viewfood/',viewfood,name='viewfood'),
    path('delete/<int:id>/',delete,name='delete'),
    path('register/',register,name='register'),
    path('viewhotal/',viewhotal,name='viewhotal')
]