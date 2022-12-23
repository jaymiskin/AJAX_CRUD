from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path('new_user/', new_user, name='new_user'),
]