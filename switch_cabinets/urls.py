from django.urls import path
from .views import SwitchCabinetsListView

app_name = 'switch_cabinets'

urlpatterns = [
    path('', SwitchCabinetsListView, name='index'),
]