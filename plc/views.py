from .models import *
from django.views.generic import ListView


class PLCListView(ListView):
    model = PLC
    template_name = 'plc/base.html'
