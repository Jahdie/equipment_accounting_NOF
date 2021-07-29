from .models import *
from django.views.generic import ListView


class PLCListView(ListView):
    model = PLC
    template_name = 'plc/index.html'


class ModulesInPLCListView(ListView):
    model = ModuleInPLC
    template_name = 'plc/modules_in_plc.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Цеха'
        context['modules_in_plc'] = ModuleInPLC.objects.filter(plc_id=self.kwargs['plc_id'])
        return context


