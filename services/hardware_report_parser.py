import openpyxl


def get_sought_data_in_hardware_report_file(path):
    """Читаем хардварные отчет, находим искомые строки формируем список и запихиваем значения в соответствующие ключи,
    так же создаем список"""
    hardware_report_dict_with_hardware_report_list = {}
    hardware_report_list = []
    hardware_report_dict = {
        'name': [],
        'ip': [],
        'racks': [],
        'slots': [],
        'models': [],
        'address': [],
        'length': [],
    }
    work_book_of_excel_file = openpyxl.load_workbook(path)
    sheet_of_work_book = work_book_of_excel_file['Лист1']
    for cell in sheet_of_work_book['A']:
        if cell.value is not None:
            cell_content_str = str(cell.value)
            cell_content_list = cell_content_str.split()
            # print(cell_content_list)
            if 'Target' in cell_content_list and 'Name:' in cell_content_list:
                hardware_report_dict['name'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            if 'IP' in cell_content_list and 'Address:' and len(cell_content_list) == 3:
                hardware_report_dict['ip'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            if 'Rack' in cell_content_list and 'Slot' not in cell_content_list:
                # print(cell_content_list)
                if cell_content_list[0] == 'Main':
                    # print(cell_content_list)
                    cell_content_list[0] = 'Rack'
                    cell_content_list[1] = '0:'
                hardware_report_dict['racks'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            first_letters_in_cell_content = cell_content_list[0][0:2]
            if first_letters_in_cell_content == 'IC' and 'fan' not in cell_content_list and 'Daughterboard' \
                    not in cell_content_list:
                hardware_report_dict['models'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            if ('Rack' in cell_content_list or 'Main' in cell_content_list) and 'Slot' in cell_content_list:
                # print(cell_content_list)
                if 'Rack:' in cell_content_list:
                    # print(cell_content_list)
                    cell_content_list[0] = 'Rack'
                    cell_content_list[1] = '0:'
                if cell_content_list[1][-1] != ':':
                    # print(cell_content_list[1])
                    cell_content_list[1] = cell_content_list[1] + ':'
                    # print(cell_content_list[1])
                hardware_report_dict['slots'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            if 'Used' in cell_content_list and 'Slot' in cell_content_list:
                hardware_report_list.append(cell_content_list)
                hardware_report_dict['models'].append(cell_content_list)
            if 'Reference' in cell_content_list and 'Address:' in cell_content_list:
                hardware_report_dict['address'].append(cell_content_list)
                hardware_report_list.append(cell_content_list)
            if 'Length:' in cell_content_list and len(cell_content_list) == 2:
                if int(cell_content_list[1]) % 2 == 0:
                    hardware_report_dict['length'].append(cell_content_list)
                    hardware_report_list.append(cell_content_list)
    hardware_report_dict_with_hardware_report_list.update(
        {'hardware_report_dict': hardware_report_dict, 'hardware_report_list': hardware_report_list})
    return hardware_report_dict_with_hardware_report_list


def get_plc_name_and_plc_ip_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list):
    """Формируем итоговый словарь, находим имя ПЛК его IP и помещаем туда"""
    hardware_report_final_dict = {
        'name': '',
        'ip': [],
        'racks': []
    }
    for item in hardware_report_dict_with_hardware_report_list['hardware_report_dict']['name']:
        plc_name = item[2]
        hardware_report_final_dict['name'] = plc_name

    for item in hardware_report_dict_with_hardware_report_list['hardware_report_dict']['ip']:
        plc_ip = item[2]
        hardware_report_final_dict['ip'].append(plc_ip)
    return hardware_report_final_dict


def get_racks_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list, hardware_report_final_dict):
    """Находим номера Racks, их модели и типы"""
    for index_dict in range(len(hardware_report_dict_with_hardware_report_list['hardware_report_dict']['racks'])):
        # print(hardware_report_dict['racks'][index_dict])
        rack_number = hardware_report_dict_with_hardware_report_list['hardware_report_dict']['racks'][index_dict][1][
                      :-1]

        rack_model = hardware_report_dict_with_hardware_report_list['hardware_report_dict']['racks'][index_dict][2][:-1]
        rack_type = ' '.join(
            hardware_report_dict_with_hardware_report_list['hardware_report_dict']['racks'][index_dict][3:])
        racks_dict = {'number': rack_number, 'model': rack_model, 'type': rack_type, 'slots': []}
        hardware_report_final_dict['racks'].append(racks_dict)
    return hardware_report_final_dict


def get_slots_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list, hardware_report_final_dict):
    """Находим номера Slots, их модели и типы"""
    for index_dict in range(len(hardware_report_dict_with_hardware_report_list['hardware_report_dict']['slots'])):
        rack_num_in_slots_temp = \
            hardware_report_dict_with_hardware_report_list['hardware_report_dict']['slots'][index_dict][1][:-1]
        # print(rack_num_in_slots_temp)
        if hardware_report_dict_with_hardware_report_list['hardware_report_dict']['slots'][index_dict][1][
           :-1] == rack_num_in_slots_temp:
            slot_num = hardware_report_dict_with_hardware_report_list['hardware_report_dict']['slots'][index_dict][3]

            if hardware_report_dict_with_hardware_report_list['hardware_report_dict']['models'][index_dict][0][-1] \
                    != ',':
                slot_model = \
                    hardware_report_dict_with_hardware_report_list['hardware_report_dict']['models'][index_dict][0]
            else:
                slot_model = \
                    hardware_report_dict_with_hardware_report_list['hardware_report_dict']['models'][index_dict][0][:-1]

            slot_type = ' '.join(
                hardware_report_dict_with_hardware_report_list['hardware_report_dict']['models'][index_dict][1:])
            if slot_model != 'Used':
                slots_dict = {'number': slot_num, 'model': slot_model, 'type': slot_type, 'reference_address': []}
                hardware_report_final_dict['racks'][int(rack_num_in_slots_temp)]['slots'].append(slots_dict)
    return hardware_report_final_dict


def get_reference_address_and_lenght_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list):
    """Формируем список списков с адрессами, их диапазоном, слотами"""
    address_and_length_in_slot_list = []
    slot_num_temp = None
    slot_model_temp = None
    for index_list in range(len(hardware_report_dict_with_hardware_report_list['hardware_report_list'])):
        address_and_length_in_slot = []
        if 'Reference' in hardware_report_dict_with_hardware_report_list['hardware_report_list'][index_list]:
            address = hardware_report_dict_with_hardware_report_list['hardware_report_list'][index_list]
            length = hardware_report_dict_with_hardware_report_list['hardware_report_list'][index_list + 1]
            slot_model = hardware_report_dict_with_hardware_report_list['hardware_report_list'][index_list - 1]
            slot_num = hardware_report_dict_with_hardware_report_list['hardware_report_list'][index_list - 2]
            # print(slot_model, slot_num, slot_model[0][0:2])
            if slot_model[0][0:2] == 'IC' and 'Slot' in slot_num:
                slot_model_temp = slot_model
                slot_num_temp = slot_num
            address_and_length_in_slot.append(slot_num_temp)
            address_and_length_in_slot.append(slot_model_temp)
            address_and_length_in_slot.append(address)
            address_and_length_in_slot.append(length)
            address_and_length_in_slot_list.append(address_and_length_in_slot)
    return address_and_length_in_slot_list


def adding_reference_address_in_hardware_report_final_dict(address_and_length_in_slot_list, hardware_report_final_dict):
    for item_in_list in address_and_length_in_slot_list:
        address_dict = {}
        # print(item_in_list)
        index_dict = 0
        rack_number = item_in_list[0][1][:-1]
        slot_number = item_in_list[0][3]
        for item_in_nested_list in item_in_list:
            if 'Slot' not in item_in_nested_list and item_in_nested_list[0][0:2] != 'IC':
                if 'Reference' in item_in_nested_list:
                    # print(item_in_nested_list)
                    address = item_in_nested_list[2]
                else:
                    length = item_in_nested_list[1]
        address_dict.update({'address': address, 'length': length})
        for item in hardware_report_final_dict['racks'][int(rack_number)]['slots']:
            index_dict += 1
            if item['number'] == slot_number:
                hardware_report_final_dict['racks'][int(rack_number)]['slots'][index_dict - 1][
                    'reference_address'].append(address_dict)
    return hardware_report_final_dict


def get_hardware_report_final_dict(path):
    hardware_report_dict_with_hardware_report_list = get_sought_data_in_hardware_report_file(path)
    hardware_report_final_dict = get_plc_name_and_plc_ip_from_hardware_report_dict(
        hardware_report_dict_with_hardware_report_list)
    hardware_report_final_dict = get_racks_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list,
                                                                     hardware_report_final_dict)
    hardware_report_final_dict = get_slots_from_hardware_report_dict(hardware_report_dict_with_hardware_report_list,
                                                                     hardware_report_final_dict)
    address_and_length_in_slot_list = get_reference_address_and_lenght_from_hardware_report_dict(
        hardware_report_dict_with_hardware_report_list)
    hardware_report_final_dict = adding_reference_address_in_hardware_report_final_dict(address_and_length_in_slot_list,
                                                                                        hardware_report_final_dict)
    return hardware_report_final_dict

