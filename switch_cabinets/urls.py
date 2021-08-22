from django.urls import path
from .views import switch_cabinets

app_name = 'switch_cabinets'

urlpatterns = [
    path('', switch_cabinets, name='index'),
]