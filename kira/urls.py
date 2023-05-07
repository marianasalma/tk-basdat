from django.urls import path
from kira.views import *

app_name = 'kira'

urlpatterns = [
    path('login', login, name='login'),
    path('', landing, name='landing'),
]