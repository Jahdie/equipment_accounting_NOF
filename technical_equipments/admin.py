from django.contrib import admin
from .models import *

MODELS_LIST = [ModuleInPLC, ModuleTypes, ControllerFamilies, RackModels, ModuleModels, TechnicalEquipments,
               TechnicalEquipmentTypes, RackTypes]

admin.site.register(MODELS_LIST)
