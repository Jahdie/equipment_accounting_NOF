from django.contrib import admin
from .models import *

MODELS_LIST = [Signals, SignalTypes, AdjustableParameters]

admin.site.register(MODELS_LIST)
