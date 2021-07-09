from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name= 'user-home'),
   # path('user-registration/',user_insurance , name='admin-user-registration'),
   path('wallet/',wallet ,name='wallet-ui'),
   path('user-insurance/',user_insurance ,name='user-insurance'),
   

]
