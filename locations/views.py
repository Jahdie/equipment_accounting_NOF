from .models import *
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from factory_equipments.models import *


class LocationsListView(ListView):
    model = Locations
    template_name = 'locations/temp.html'

    productions_list = []
    productions_name = []
    workshops_list = []
    workshops_name = []
    workshops_dict = {}
    compartments_dict = {}
    locations_dict = {}
    for location in Locations.objects.all():
        production_id_name = []
        if location.production.name not in productions_name:
            production_id_name.append(location.production.name)
            production_id_name.append(location.production.id)
            productions_list.append(production_id_name)
            productions_name.append(location.production.name)
    # print(productions_list)
    for production in productions_list:
        workshops_list = []
        for location in Locations.objects.filter(production_id=production[1]):
            workshop_id_name = []
            if location.workshop.name not in workshops_name:
                workshops_name.append(location.workshop.name)
                workshop_id_name.append(location.workshop.name)
                workshop_id_name.append(location.workshop.id)
                workshops_list.append(workshop_id_name)
                workshops_dict.update({tuple(production): workshops_list})

    for key, values in workshops_dict.items():
        compartments_list = []
        for value in values:
            compartments_list = []
            for location in Locations.objects.filter(workshop_id=value[1]):
                compartments_name = []
                compartment_id_name = []
                if location.compartment.name not in compartments_name:
                    compartments_name.append(location.compartment.name)
                    compartment_id_name.append(location.compartment.name)
                    compartment_id_name.append(location.compartment.id)
                    compartments_list.append(compartment_id_name)
                    compartments_dict.update({tuple(value): compartments_list})

    for key, values in workshops_dict.items():
        locations_list = []
        for value in values:
            if tuple(value) in compartments_dict.keys():
                locations_list.append({tuple(value): compartments_dict[tuple(value)]})
                locations_dict.update({tuple(key): locations_list})

    extra_context = {'locations': locations_dict}


def workshops_by_production(request, pk):
    if request.is_ajax():
        locations_list = []
        workshops_list = []

        for item in Locations.objects.filter(production_id=pk):
            if item.workshop.name not in workshops_list:
                workshops_list.append(item.workshop.name)
                locations_list.append(item)

        context = {'locations': locations_list}
        # print(workshops_list)
        result = render_to_string('locations/equipments_by_location.html', context)
        return JsonResponse({'result': result})


def equipments_by_location(request, production_id, workshop_id, compartment_id):
    for item in Equipments.objects.all():
        print(item.plc_name.ip)
    context = {}
    if request.is_ajax():
        if compartment_id == 0 and workshop_id == 0:
            # print("111")
            context = {'equipments': Equipments.objects.filter(location__production_id=production_id)}
        if workshop_id != 0 and compartment_id == 0:
            context = {'equipments': Equipments.objects.filter(location__production_id=production_id,
                                                               location__workshop_id=workshop_id)}
        if workshop_id != 0 and compartment_id != 0:
            context = {'equipments': Equipments.objects.filter(location__production_id=production_id,
                                                               location__workshop_id=workshop_id,
                                                               location__compartment_id=compartment_id)}
        # print(production_id, workshop_id, compartment_id)
        # print(Equipments.objects.filter(location__production_id=production_id))


        # print(context["locations"])
        result = render_to_string('locations/equipments_by_location.html', context)
        return JsonResponse({'result': result})
