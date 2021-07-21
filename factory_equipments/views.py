from .models import *
from django.views.generic import ListView


class FactoryEquipmentListView(ListView):
    model = EquipmentNames
    template_name = 'locations/base.html'
    Equipments.objects.create(equipment_name_id=453, equipment_model_id=201, equipment_type_id=129)
