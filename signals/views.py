from .models import *
from django.views.generic import ListView
from switch_cabinets.models import SwitchPorts
from django.shortcuts import render, redirect
from technical_equipments.models import TechnicalEquipments, RackModels, ControllerFamilies, ModuleTypes, ModuleModels, \
    TechnicalEquipmentTypes, RackTypes
from services import hardware_report_parser
from signals.models import Signals


def signals(request):
    context = {}
    # SwitchPorts.objects.all().delete()
    # Signals.objects.all().delete()
    # ModuleInPLC.objects.all().delete()
    # TechnicalEquipments.objects.all().delete()


    # for path in hardware_report_parser.get_path_to_excel_file('D:\\config plc'):
    #     cell_content_list = hardware_report_parser.get_list_from_hardware_report(path)
    #     rack_list = hardware_report_parser.get_list_of_lists_from_cell_content_list(cell_content_list)
    #     hardware_report_dict = hardware_report_parser.get_hardware_report_dict(rack_list)
    #     # print(hardware_report_dict)
    #     if not TechnicalEquipments.objects.filter(name=hardware_report_dict['name'],
    #                                               project=hardware_report_dict['project']).exists():
    #         technical_equipment_type_id = TechnicalEquipmentTypes.objects.get(name='PLC').id
    #         if not hardware_report_dict['ip']:
    #             ip = None
    #         else:
    #             ip = hardware_report_dict['ip'][0]
    #         TechnicalEquipments.objects.create(name=hardware_report_dict['name'],
    #                                            ip=ip,
    #                                            technical_equipment_type_id=technical_equipment_type_id,
    #                                            project=hardware_report_dict['project'], location_id=1)
    #         technical_equipment_id = TechnicalEquipments.objects.get(
    #             name=hardware_report_dict['name'],
    #             project=hardware_report_dict['project']).id
    #         SwitchPorts.objects.create(technical_equipment_id=technical_equipment_id, port_num=1, switch_id=1)
    #     for rack in hardware_report_dict['racks']:
    #         # print(rack['model'], rack['type'])
    #         if not RackTypes.objects.filter(name=rack['type']).exists():
    #             RackTypes.objects.create(name=rack['type'])
    #         if not RackModels.objects.filter(name=rack['model']).exists():
    #             rack_type_id = RackTypes.objects.get(name=rack['type']).id
    #             RackModels.objects.create(name=rack['model'], rack_type_id=rack_type_id)
    #         for slot in rack['slots']:
    #             # print(slot)
    #             if not ModuleTypes.objects.filter(name=slot['type']).exists():
    #                 ModuleTypes.objects.create(name=slot['type'])
    #             if not ModuleModels.objects.filter(name=slot['model']).exists():
    #                 slot_type_id = ModuleTypes.objects.get(name=slot['type']).id
    #                 ModuleModels.objects.create(name=slot['model'], module_type_id=slot_type_id)
    #
    #     for rack in hardware_report_dict['racks']:
    #         for slot in rack['slots']:
    #             plc_id = TechnicalEquipments.objects.get(name=hardware_report_dict['name'],
    #                                                      project=hardware_report_dict['project']).id
    #             slot_type_id = ModuleTypes.objects.get(name=slot['type']).id
    #             slot_model_id = ModuleModels.objects.get(name=slot['model']).id
    #             rack_model_id = RackModels.objects.get(name=rack['model']).id
    #             rack_number = rack['number']
    #             slot_number = slot['number']
    #             reference_address = slot['reference_address']
    #             # print(rack['number'])
    #             if not ModuleInPLC.objects.filter(rack=rack_number, slot=slot_number, rack_model_id=rack_model_id,
    #                                               module_type_id=slot_type_id, module_model_id=slot_model_id,
    #                                               reference_address=reference_address, plc_id=plc_id):
    #                 ModuleInPLC.objects.create(rack=rack_number, slot=slot_number, rack_model_id=rack_model_id,
    #                                            module_type_id=slot_type_id, module_model_id=slot_model_id,
    #                                            reference_address=reference_address, plc_id=plc_id)
    #
    # for path in hardware_report_parser.get_path_to_excel_file('D:\\PROSCON'):
    #     point_dict = hardware_report_parser.get_address_of_point(path)
    #     for point in point_dict['point']:
    #         point_id = point['point_id']
    #         address = point['address']
    #         description = point['description']
    #         project = 'NOF' + point_id[0:3]
    #         # print(project)
    #         module_id = ModuleInPLC.get_module_id_by_signal_input_reg(signal_address=address, project=project)
    #         print(module_id, project)
    #         if module_id is not None:
    #             if not Signals.objects.filter(name=point_id).exists():
    #                 Signals.objects.create(name=point_id, address=address, module_id=module_id, description=description)
    #                     # print(module_id, input_reg, point_id)

    return render(request, 'signals/index.html', context)
