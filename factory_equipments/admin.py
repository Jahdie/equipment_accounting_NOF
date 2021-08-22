from django.contrib import admin
from .models import *
MODELS_LIST = [EquipmentTypes, EquipmentNames, AutomationComplex, Equipments]

admin.site.register(MODELS_LIST)
