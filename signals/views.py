from .models import *
from django.views.generic import ListView
import openpyxl
from django.shortcuts import render, redirect
from technical_equipments.models import TechnicalEquipments, RackModels, ControllerFamilies, ModuleTypes, ModuleModels, \
    TechnicalEquipmentTypes, RackTypes
from services import hardware_report_parser
from signals.models import Signals


def signals(request):
    context = {}
    for path in hardware_report_parser.get_path_to_excel_file('D:\\config plc'):
        cell_content_list = hardware_report_parser.get_list_from_hardware_report(path)
        rack_list = hardware_report_parser.get_list_of_lists_from_cell_content_list(cell_content_list)
        hardware_report_dict = hardware_report_parser.get_hardware_report_dict(rack_list)
        print(hardware_report_dict)
    # modules_in_plc_and_plc_name_and_plc_ip = hardware_report_parser.get_hardware_report_final_dict('D:\\1.xlsx')
    # # for racks in modules_in_plc_and_plc_name_and_plc_ip['racks']:
    # #     for slots in racks['slots']:
    # #         print(slots)
    #
    # if not TechnicalEquipments.objects.filter(name=modules_in_plc_and_plc_name_and_plc_ip['name']).exists():
    #     technical_equipment_type_id = TechnicalEquipmentTypes.objects.get(name='PLC').id
    #     # print(technical_equipment_type_id)
    #     TechnicalEquipments.objects.create(name=modules_in_plc_and_plc_name_and_plc_ip['name'],
    #                                        ip=modules_in_plc_and_plc_name_and_plc_ip['ip'][0],
    #                                        technical_equipment_type_id=technical_equipment_type_id)
    # for rack in modules_in_plc_and_plc_name_and_plc_ip['racks']:
    #     # print(rack['model'], rack['type'])
    #     if not RackTypes.objects.filter(name=rack['type']).exists():
    #         RackTypes.objects.create(name=rack['type'])
    #     if not RackModels.objects.filter(name=rack['model']).exists():
    #         rack_type_id = RackTypes.objects.get(name=rack['type']).id
    #         RackModels.objects.create(name=rack['model'], rack_type_id=rack_type_id)
    #     for slot in rack['slots']:
    #         # print(slot)
    #         if not ModuleTypes.objects.filter(name=slot['type']).exists():
    #             ModuleTypes.objects.create(name=slot['type'])
    #         if not ModuleModels.objects.filter(name=slot['model']).exists():
    #             slot_type_id = ModuleTypes.objects.get(name=slot['type']).id
    #             ModuleModels.objects.create(name=slot['model'], module_type_id=slot_type_id)
    #
    # for rack in modules_in_plc_and_plc_name_and_plc_ip['racks']:
    #     for slot in rack['slots']:
    #         plc_id = TechnicalEquipments.objects.get(name=modules_in_plc_and_plc_name_and_plc_ip['name']).id
    #         slot_type_id = ModuleTypes.objects.get(name=slot['type']).id
    #         slot_model_id = ModuleModels.objects.get(name=slot['model']).id
    #         rack_model_id = RackModels.objects.get(name=rack['model']).id
    #         rack_number = rack['number']
    #         slot_number = slot['number']
    #         reference_address = slot['reference_address']
    #         # print(rack['number'])
    #         if not ModuleInPLC.objects.filter(rack=rack_number, slot=slot_number, rack_model_id=rack_model_id,
    #                                           module_type_id=slot_type_id, module_model_id=slot_model_id,
    #                                           reference_address=reference_address, plc_id=plc_id):
    #             ModuleInPLC.objects.create(rack=rack_number, slot=slot_number, rack_model_id=rack_model_id,
    #                                        module_type_id=slot_type_id, module_model_id=slot_model_id,
    #                                        reference_address=reference_address, plc_id=plc_id)
    #     work_book_of_excel_file = openpyxl.load_workbook('D:\\NOFAC1_Q_Points.xlsx')
    #     sheet_of_work_book = work_book_of_excel_file.active
    #     for row in sheet_of_work_book.iter_rows():
    #         point_id = row[0].value
    #         description = row[1].value
    #         input_reg = row[30].value
    #         # print(input_reg)
    #         module_id = ModuleInPLC.get_module_id_by_signal_input_reg(signal_address=input_reg)
    #         # print(module_id, input_reg, point_id)
    #         if module_id is not None:
    #             if not Signals.objects.filter(name=point_id).exists():
    #                 Signals.objects.create(name=point_id, input_reg=input_reg, module_id=module_id)
    #                 # print(module_id, input_reg, point_id)
    #         # print(point_id, description, input_reg)
    #
    #     # for address in slot['reference_address']:
    #     #     print(address['address'])
    #
    # # for item in ModuleInPLC.objects.all():
    # #     print(item.reference_address)
    # # print(ModuleInPLC.get_module_id_by_signal_input_reg(self=None, signal_address='%AQ00060'))
    return render(request, 'signals/index.html', context)
