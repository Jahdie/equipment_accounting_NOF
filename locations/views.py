from .models import *
from django.views.generic import ListView


class LocationsListView(ListView):
    model = Locations
    template_name = 'locations/base.html'
