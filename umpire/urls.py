from django.urls import path
from umpire.views import *

app_name = 'wishlist'

urlpatterns = [
    path('perempat', show_perempat, name='show_perempat'),
    path('list-event', list_event, name='list_event'),
]
