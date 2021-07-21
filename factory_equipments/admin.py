from django.contrib import admin
from .models import *
MODELS_LIST = [EquipmentTypes, EquipmentNames, EquipmentModels, AutomationComplex, DeviceName, Equipments]

admin.site.register(MODELS_LIST)
