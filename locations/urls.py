from django.urls import path
from .views import *

app_name = 'locations'

urlpatterns = [
    path('', LocationsListView.as_view(), name='index'),
    path('<int:production_id>/<int:workshop_id>/<int:compartment_id>/', equipments_by_location,
         name='equipments_by_location,'),
    # path('workshops/<int:pk>/', compartments_by_workshop, name='compartments_by_workshops'),
]
