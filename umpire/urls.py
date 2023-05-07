from django.urls import path
from umpire.views import show_perempat

app_name = 'wishlist'

urlpatterns = [
    path('perempat', show_perempat, name='show_perempat'),
]
