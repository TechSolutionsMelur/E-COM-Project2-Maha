from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('addfood/<int:restaurant_id>/',addfood,name='addfood'),
    path('viewmenu/<int:restaurant_id>/',view_menu,name='viewmenu'),
    path('delete/<int:id>/',delete,name='delete'),
    path('addrestaurant/',addrestaurant,name='addrestaurant'),
    path('restaurant_list/',restaurant_list,name='restaurant_list'),
    path('update/<int:id>/',update,name='update')
]