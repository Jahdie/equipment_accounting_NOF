from django.urls import path
from .views import *

app_name = 'signals'

urlpatterns = [
    path('', PLCListView.as_view(), name='index'),
    path('<int:plc_id>/', ModulesInPLCListView.as_view(), name='modules_in_plc'),
]