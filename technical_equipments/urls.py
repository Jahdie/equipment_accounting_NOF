from django.urls import path
from .views import *

app_name = 'technical_equipments'

urlpatterns = [
    path('', PLCListView.as_view(), name='index'),
    path('<int:plc_id>/', modules_in_plc, name='modules_in_plc'),
    path('<int:plc_id>/<int:rack_id>/<int:slot_id>/', signals_in_module, name='signals_in_module'),
]
