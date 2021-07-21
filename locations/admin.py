from django.contrib import admin
from .models import *

MODELS_LIST = [Locations, Productions, Workshops, Compartments]

admin.site.register(MODELS_LIST)