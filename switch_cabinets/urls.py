from django.urls import path
from .views import switch_cabinets, ports_in_switch

app_name = 'switch_cabinets'

urlpatterns = [
    path('<int:switch_cabinet_id>/', switch_cabinets, name='switch_cabinet'),
    path('<int:switch_cabinet_id>/<int:switch_id>/', ports_in_switch, name='ports_in_switch'),
]