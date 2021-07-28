from .models import *
from django.views.generic import ListView


class FactoryEquipmentListView(ListView):
    model = EquipmentNames
    template_name = 'locations/base.html'
