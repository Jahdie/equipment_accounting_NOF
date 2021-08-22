from .models import *
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from factory_equipments.models import *
from technical_equipments.models import *


def locations(request):
    for item in TechnicalEquipments.objects.all():
        for item1 in item.switchports_set.filter(technical_equipment=item.id):
            print(item1.switch.switch_cabinet)
    context = {}
    locations_dict_list = []
    for production in Locations.objects.distinct('production'):
        workshop_dicts_list = []
        locations_dict = {}
        locations_dict.update(
            {'production_name': production.production.name, 'production_id': production.production.id})
        locations_dict_list.append(locations_dict)

        for workshop in Locations.objects.filter(production_id=production.production_id).distinct('workshop_id'):
            compartments_dict_list = []
            workshops_dict = {}
            workshops_dict.update(
                {'workshop_name': workshop.workshop.name, 'workshop_id': workshop.workshop.id})
            workshop_dicts_list.append(workshops_dict)
            locations_dict.update({'workshops': workshop_dicts_list})

            for compartment in Locations.objects.filter(production=workshop.production.id,
                                                        workshop=workshop.workshop.id):
                compartments_dict = {}
                compartments_dict.update(
                    {'compartment_name': compartment.compartment.name, 'compartment_id': compartment.compartment.id})
                compartments_dict_list.append(compartments_dict)
                workshops_dict.update({'compartments': compartments_dict_list})

    context.update({'locations': locations_dict_list})
    return render(request, 'locations/index.html', context)


def equipments_by_location(request, production_id, workshop_id, compartment_id):
    context = {}
    # equipments_dict = {}

    if request.is_ajax():
        if compartment_id == 0 and workshop_id == 0:
            equipments_dicts_list = []
            for item in TechnicalEquipments.objects.filter(location__production_id=production_id):
                equipments_dict = {}
                print(item)
                for item1 in item.switchports_set.filter(technical_equipment=item.id):
                    # print(item1.switch.switch_cabinet)
                    equipments_dict.update({'equipment_name': item.name})
                    equipments_dict.update({'equipment_id': item.id})
                    equipments_dict.update({'equipment_ip': item.ip})
                    equipments_dict.update({'equipment_type': item.technical_equipment_type.name})
                    equipments_dict.update({'switch_cabinet': item1.switch.switch_cabinet})
                    equipments_dicts_list.append(equipments_dict)


        if workshop_id != 0 and compartment_id == 0:
            equipments_dicts_list = []
            for item in TechnicalEquipments.objects.filter(location__production_id=production_id,
                                                           location__workshop_id=workshop_id):
                equipments_dict = {}
                for item1 in item.switchports_set.filter(technical_equipment=item.id):
                    print(item1.switch.switch_cabinet)
                    equipments_dict.update({'equipment_name': item.name})
                    equipments_dict.update({'equipment_id': item.id})
                    equipments_dict.update({'equipment_ip': item.ip})
                    equipments_dict.update({'equipment_type': item.technical_equipment_type.name})
                    equipments_dict.update({'switch_cabinet': item1.switch.switch_cabinet})
                    equipments_dicts_list.append(equipments_dict)

        if workshop_id != 0 and compartment_id != 0:
            equipments_dicts_list = []
            for item in TechnicalEquipments.objects.filter(location__production_id=production_id,
                                                           location__workshop_id=workshop_id,
                                                           location__compartment_id=compartment_id):
                equipments_dict = {}
                for item1 in item.switchports_set.filter(technical_equipment=item.id):
                    print(item1.switch.switch_cabinet)
                    equipments_dict.update({'equipment_name': item.name})
                    equipments_dict.update({'equipment_id': item.id})
                    equipments_dict.update({'equipment_ip': item.ip})
                    equipments_dict.update({'equipment_type': item.technical_equipment_type.name})
                    equipments_dict.update({'switch_cabinet': item1.switch.switch_cabinet})
                    equipments_dicts_list.append(equipments_dict)
        context.update({'technical_equipments': equipments_dicts_list})
        result = render_to_string('locations/equipments_by_location.html', context)
        return JsonResponse({'result': result})
