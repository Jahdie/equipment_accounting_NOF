from django.contrib import admin
from .models import *

MODELS_LIST = [Productions, Workshops, Compartments, Locations]

admin.site.register(MODELS_LIST)
