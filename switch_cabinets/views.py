from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from factory_equipments.models import *
from technical_equipments.models import *


def switch_cabinets(request, switch_cabinet_id):
    context = {}
    switch_cabinet_dicts_list = []
    for el in SwitchCabinets.objects.filter(id=switch_cabinet_id):
        switch_dicts_list = []
        switch_cabinet_dict = {}
        switch_cabinet_dict.update({'switch_cabinet_id': el.id})
        switch_cabinet_dict.update({'switch_cabinet_name': el.name})

        for item in Switches.objects.filter(switch_cabinet=el.id):
            switch_dict = {}
            switch_dict.update({'switch_model': item.model})
            switch_dict.update({'switch_id': item.id})
            switch_dict.update({'switch_ip': item.ip})

            switch_dicts_list.append(switch_dict)
            switch_cabinet_dict.update({'switches': switch_dicts_list})
    context.update({'switches': switch_cabinet_dict})
    context.update({'switch_cabinets': SwitchCabinets.objects.all()})
    print(switch_cabinet_dict)
    print(context['switches'])

    return render(request, 'switch_cabinets/index.html', context)


def ports_in_switch(request, switch_cabinet_id, switch_id):
    context = {}
    equipments_dict_list = []
    if request.is_ajax():
        context.update({'ports': SwitchPorts.objects.filter(switch_id=switch_id)})
        result = render_to_string('switch_cabinets/ports_in_switch.html', context)
        print(context)
        return JsonResponse({'result': result})
