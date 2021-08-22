from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from signals.models import Signals


def factory_equipments(request):
    context = {}
    equipments_dict_list = []
    for item in Equipments.objects.distinct('automation_complex'):
        equipments_type_dicts_list = []
        automations_dict = {}
        automations_dict.update(
            {'automation_name': item.automation_complex.name, 'automation_id': item.automation_complex_id})
        equipments_dict_list.append(automations_dict)

        for item1 in Equipments.objects.filter(automation_complex=item.automation_complex).distinct('equipment_type'):
            equipments_name_dict_list = []
            equipments_type_dict = {}
            equipments_type_dict.update(
                {'equipment_type_name': item1.equipment_type.name, 'equipment_type_id': item1.equipment_type_id})
            equipments_type_dicts_list.append(equipments_type_dict)
            automations_dict.update({'equipments_type': equipments_type_dicts_list})

            for item2 in Equipments.objects.filter(automation_complex__name=item.automation_complex.name,
                                                   equipment_type=item1.equipment_type):
                equipments_name_dict = {}
                equipments_name_dict.update(
                    {'equipment_name': item2.equipment_name.name, 'equipment_id': item2.equipment_name_id})
                equipments_name_dict_list.append(equipments_name_dict)
                equipments_type_dict.update({'equipments_name': equipments_name_dict_list})

    context.update({'equipments': equipments_dict_list})
    return render(request, 'factory_equipments/index.html', context)


def signals_by_equipment(request, automation_id, equipment_type_id, equipment_name_id):
    context = {}
    if request.is_ajax():
        if equipment_type_id == 0 and equipment_name_id == 0:
            context.update({'signals': Signals.objects.filter(equipment__automation_complex=automation_id)})
        if equipment_type_id != 0 and equipment_name_id == 0:
            context.update({'signals': Signals.objects.filter(equipment__automation_complex=automation_id,
                                                              equipment__equipment_type=equipment_type_id)})
        if equipment_type_id != 0 and equipment_name_id != 0:
            context.update({'signals': Signals.objects.filter(equipment__automation_complex=automation_id,
                                                              equipment__equipment_type=equipment_type_id,
                                                              equipment__equipment_name=equipment_name_id)})
        result = render_to_string('factory_equipments/signals_by_equipment.html', context)
        return JsonResponse({'result': result})
