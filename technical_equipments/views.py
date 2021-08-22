from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from signals.models import Signals


class PLCListView(ListView):
    model = ModuleInPLC
    template_name = 'plc/index.html'


def modules_in_plc(request, plc_id):
    rack_names = []
    modules = {}
    for module in ModuleInPLC.objects.filter(plc_id=plc_id):
        if module.rack not in rack_names:
            rack_names.append(module.rack)
    for rack in rack_names:
        rack_and_plc_id = ()
        rack_and_plc_id = (rack, plc_id)
        modules_name = []
        modules_name.append(ModuleInPLC.objects.filter(plc_id=plc_id, rack=rack))
        modules.update({rack_and_plc_id: modules_name})
    context = {'modules_plc': modules, 'plc_id': plc_id}
    return render(request, 'plc/modules_in_plc.html', context)


def signals_in_module(request, plc_id, rack_id, slot_id):
    if request.is_ajax():
        signals_list = []
        if slot_id == 9999999:
            module_list = []
            for module in ModuleInPLC.objects.filter(plc_id=plc_id, rack=rack_id):
                module_list.append(module)

        else:
            module_list = []
            for module in ModuleInPLC.objects.filter(plc_id=plc_id, rack=rack_id, slot=slot_id):
                module_list.append(module)
        context = {'modules': module_list}
        for module in module_list:
            for signal in Signals.objects.filter(module_id=module.id):
                signals_list.append(signal)

        context = {'signals': signals_list}
        result = render_to_string('plc/signals_in_module.html', context)
        return JsonResponse({'result': result})
