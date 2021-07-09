from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name='admin-home'),
    path('user-list/',user_list , name='admin-user-list'),
    path('user-registration/',user_registration , name='admin-user-registration'),
    path('user-update/<str:n>/',user_update , name='admin-user-update'),
    path('number_plate_detection/',number_plate_detection,name='number_plate_detection'),
    path('number-plate-check/',check,name='number-plate-check'),
    path('number-plate-check2/',check2,name='number-plate-check2')

    
]
