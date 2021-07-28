from django.contrib import admin
from switch_cabinets.models import *

MODELS_LIST = [SwitchModels, SwitchPorts, Switches, SwitchCabinets]

admin.site.register(MODELS_LIST)
