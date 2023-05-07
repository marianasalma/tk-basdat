from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('atlet', show_dashboard_atlet, name='dash_atlet'),
    path('pelatih', show_dashboard_pelatih, name='dash_pelatih'),
    path('umpire', show_dashboard_umpire, name='dash_umpire'),
]