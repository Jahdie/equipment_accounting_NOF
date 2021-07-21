from django.urls import path
from .views import FactoryEquipmentListView

app_name = 'factory_equipments'

urlpatterns = [
    path('', FactoryEquipmentListView.as_view(), name='index'),
]