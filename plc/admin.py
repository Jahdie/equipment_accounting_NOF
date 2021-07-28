from django.contrib import admin
from .models import *

MODELS_LIST = [PLC, ModuleInPLC, ModuleTypes, ControllerFamilies, RackModels, ModuleModels]

admin.site.register(MODELS_LIST)
