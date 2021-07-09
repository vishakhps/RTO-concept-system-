from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('login/', loginpage, name="login"),
    path('register/', register, name="user-register"),
    path('logout/', logoutUser, name="logout"),
]
