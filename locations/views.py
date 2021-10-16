from .models import *
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from factory_equipments.models import *
from technical_equipments.models import *


def locations(request):
    context = {}
    locations_dict_list = Locations.get_locations_hierarchy()

    context.update({'locations': locations_dict_list})
    return render(request, 'locations/index.html', context)


def equipments_by_location(request, production_id, workshop_id, compartment_id):
    context = {}
    equipments_dict_list = []
    if request.is_ajax():
        if compartment_id == 0 and workshop_id == 0:
            equipments_dict_list = []
            for item in TechnicalEquipments.objects.filter(location__production=production_id):
                equipments_dict = {}
                for item1 in item.switchports_set.filter(switch__switch_cabinet__location__production=production_id):
                    equipments_dict.update({'project': item.project})
                    equipments_dict.update({'technical_equipment_name': item.name})
                    equipments_dict.update({'technical_equipment_id': item.id})
                    equipments_dict.update({'technical_equipment_ip': item.ip})
                    equipments_dict.update({'technical_equipment_type': item.technical_equipment_type})
                    equipments_dict.update({'switch_cabinet_name': item1.switch.switch_cabinet.name})
                    equipments_dict.update({'switch_cabinet_id': item1.switch.switch_cabinet.id})
                    equipments_dict_list.append(equipments_dict)

        if compartment_id == 0 and workshop_id != 0:
            equipments_dict_list = []
            for item in TechnicalEquipments.objects.filter(location__production=production_id,
                                                           location__workshop=workshop_id):
                equipments_dict = {}
                for item1 in item.switchports_set.filter(technical_equipment=item.id):
                    equipments_dict.update({'project': item.project})
                    equipments_dict.update({'technical_equipment_name': item.name})
                    equipments_dict.update({'technical_equipment_id': item.id})
                    equipments_dict.update({'technical_equipment_ip': item.ip})
                    equipments_dict.update({'technical_equipment_type': item.technical_equipment_type})
                    equipments_dict.update({'switch_cabinet_name': item1.switch.switch_cabinet.name})
                    equipments_dict.update({'switch_cabinet_id': item1.switch.switch_cabinet.id})
                    equipments_dict_list.append(equipments_dict)

        if compartment_id != 0 and workshop_id != 0:
            equipments_dict_list = []
            for item in TechnicalEquipments.objects.filter(location__production=production_id,
                                                           location__workshop=workshop_id,
                                                           location__compartment=compartment_id):
                equipments_dict = {}
                for item1 in item.switchports_set.filter(technical_equipment=item.id):
                    equipments_dict.update({'project': item.project})
                    equipments_dict.update({'technical_equipment_name': item.name})
                    equipments_dict.update({'technical_equipment_id': item.id})
                    equipments_dict.update({'technical_equipment_ip': item.ip})
                    equipments_dict.update({'technical_equipment_type': item.technical_equipment_type})
                    equipments_dict.update({'switch_cabinet_name': item1.switch.switch_cabinet.name})
                    equipments_dict.update({'switch_cabinet_id': item1.switch.switch_cabinet.id})
                    equipments_dict_list.append(equipments_dict)
                # print(equipments_dict)
            print(equipments_dict_list)

        context.update({'technical_equipments': equipments_dict_list})
        result = render_to_string('locations/equipments_by_location.html', context)
        return JsonResponse({'result': result})
