from django.urls import path
from .views import factory_equipments, signals_by_equipment

app_name = 'factory_equipments'

urlpatterns = [
    path('', factory_equipments, name='index'),
    path('<int:automation_id>/<int:equipment_type_id>/<int:equipment_name_id>/', signals_by_equipment, name='index'),
]
