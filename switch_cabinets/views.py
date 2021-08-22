from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from factory_equipments.models import *
from technical_equipments.models import *


def switch_cabinets(request):
    context = {}
    switch_cabinet_dicts_list = []

    for item in SwitchCabinets.objects.all():
        switch_dicts_list = []
        switch_cabinet_dict = {}
        switch_cabinet_dict.update(
            {'switch_cabinet_name': item.name, 'switch_cabinet_id': item.id, 'switches': []})
        switch_cabinet_dicts_list.append(switch_cabinet_dict)
        for item1 in Switches.objects.filter(switch_cabinet=item.id):
            switches_dict = {}
            switch_dicts_list.append(switches_dict)
            print(item1.ip)
            switches_dict.update({'switch_model': item1.model, 'switch_ip': item1.ip})
            switch_cabinet_dict.update({'switches': switch_dicts_list})

    print(switch_cabinet_dicts_list)

    return render(request, 'switch_cabinets/index.html', context)
