from .models import *
from django.views.generic import ListView
import openpyxl
from django.shortcuts import render, redirect
from technical_equipments.models import TechnicalEquipments, RackModels, ControllerFamilies, ModuleTypes, ModuleModels, \
    TechnicalEquipmentTypes, RackTypes
from services import hardware_report_parser


def signals(request):
    context = {}
    modules_in_plc_and_plc_name_and_plc_ip = hardware_report_parser.get_hardware_report_final_dict('D:\\1.xlsx')
    # modules_in_plc_and_plc_name_and_plc_ip = hardware_report_parser.parsing_machine_edition_hardware_report(
    #     'D:\\1.xlsx')
    #
    # # print(modules_in_plc_and_plc_name_and_plc_ip['name'])
    if not TechnicalEquipments.objects.filter(name=modules_in_plc_and_plc_name_and_plc_ip['name']).exists():
        technical_equipment_type_id = TechnicalEquipmentTypes.objects.get(name='PLC').id
        # print(technical_equipment_type_id)
        TechnicalEquipments.objects.create(name=modules_in_plc_and_plc_name_and_plc_ip['name'],
                                           ip=modules_in_plc_and_plc_name_and_plc_ip['ip'][0],
                                           technical_equipment_type_id=technical_equipment_type_id)
    for rack in modules_in_plc_and_plc_name_and_plc_ip['racks']:
        # print(rack['model'], rack['type'])
        if not RackTypes.objects.filter(name=rack['type']).exists():
            RackTypes.objects.create(name=rack['type'])
        if not RackModels.objects.filter(name=rack['model']).exists():
            rack_type_id = RackTypes.objects.get(name=rack['type']).id
            RackModels.objects.create(name=rack['model'], rack_type_id=rack_type_id)
        for slot in rack['slots']:
            # print(slot)
            if not ModuleTypes.objects.filter(name=slot['type']).exists():
                ModuleTypes.objects.create(name=slot['type'])
            if not ModuleModels.objects.filter(name=slot['model']).exists():
                slot_type_id = ModuleTypes.objects.get(name=slot['type']).id
                ModuleModels.objects.create(name=slot['model'], module_type_id=slot_type_id)
    for rack in modules_in_plc_and_plc_name_and_plc_ip['racks']:
        for slot in rack['slots']:
            print(slot)

    return render(request, 'signals/index.html', context)
