from .models import *
from django.views.generic import ListView


class SwitchCabinetsListView(ListView):
    model = SwitchCabinets
    template_name = 'switch_cabinets/base.html'
