import os
import openpyxl


def get_path_to_excel_file(directory):
    path_list = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path_list.append(root + '\\' + filename)
    # print(path_list)
    return path_list


def get_list_from_hardware_report(path):
    # print(path)
    cell_content_list = []
    work_book_of_excel_file = openpyxl.load_workbook(path)
    sheet_of_work_book = work_book_of_excel_file['Лист1']
    for cell in sheet_of_work_book['A']:
        if cell.value is not None:
            cell_content_str = str(cell.value)
            cell_content_list.append(cell_content_str.split())

    return cell_content_list


def get_list_of_lists_from_cell_content_list(cell_content_list):
    rack_index = 0
    rack_list = []
    for index in range(len(cell_content_list)):
        rack_index_start = rack_index
        # print(cell_content_list[index])
        if ('Rack' in cell_content_list[index] or 'Rack:' in cell_content_list[index]) \
                and 'Loss' not in cell_content_list[index]:
            rack_index = index
            # print(rack_index_start, rack_index)
            rack_list.append(cell_content_list[rack_index_start:rack_index])
    rack_list.append(cell_content_list[rack_index:])
    return rack_list


def get_hardware_report_dict(rack_list):
    hardware_report_dict = {
        'name': '',
        'ip': [],
        'racks': []
    }
    for item in rack_list:
        # print(item)
        for element in item:
            if 'Name:' in element and 'Target' in element:
                plc_name = element[2]
                hardware_report_dict['name'] = plc_name
            if 'IP' in element and 'Address:' in element and len(element) == 3:
                ip = element[2]
                hardware_report_dict['ip'].append(element[2])
            if 'Rack' in element or 'Rack:' in element:
                # print(element)
                if 'Loss' not in element:
                    # print(element)
                    if element[2] != 'Slot':
                        # print(element)
                        rack_model = element[2][:-1]
                        rack_type = ' '.join(element[3:])
                        rack_number = element[1][:-1]
                        if rack_number == 'Rack':
                            rack_number = '0'
                        hardware_report_dict['racks'].append(
                            {'number': rack_number, 'type': rack_type, 'model': rack_model, 'slots': []})
            if ('Rack' in element or 'Rack:' in element) and 'Slot' in element:
                # print(element)
                rack_number = element[1][:-1]
                if rack_number == 'Rack':
                    rack_number = '0'
                if rack_number == '':
                    rack_number = element[1]
                slot_number = element[3]
                if 'Used' not in item[1] and '3RD' not in item[1]:
                    # print(item[1])
                    slot_model = item[1][0][:-1]
                    slot_type = ' '.join(item[1][2:])
                    if item[1][0][-1] != ',':
                        slot_model = item[1][0]
                    # print(slot_model, slot_type)
                    hardware_report_dict['racks'][int(rack_number)]['slots'].append(
                        {'number': slot_number, 'type': slot_type, 'model': slot_model, 'reference_address': []})
                    index_slots = len(hardware_report_dict['racks'][int(rack_number)]['slots']) - 1
                    for el in item:
                        reference_address = []
                        # print(len(hardware_report_dict['racks'][int(rack_number)]['slots'][index_slots][
                        #                 'reference_address']))
                        index_reference_address = len(
                            hardware_report_dict['racks'][int(rack_number)]['slots'][index_slots][
                                'reference_address'])
                        if 'Reference' in el and 'Address:' in el:
                            # print(el)
                            index_rack_list = item.index(el)
                            # print(item.index(el))
                            # print(item[index_rack_list], item[index_rack_list + 1])
                            address = item[index_rack_list][2]
                            length = item[index_rack_list + 1][1]
                            hardware_report_dict['racks'][int(rack_number)]['slots'][index_slots][
                                'reference_address'].append({'address': address, 'length': length})

    return hardware_report_dict

# for path in get_path_to_excel_file('D:\\config plc'):
#     cell_content_list = get_list_from_hardware_report(path)
#     rack_list = get_list_of_lists_from_cell_content_list(cell_content_list)
#     hardware_report_dict = get_hardware_report_dict(rack_list)
#     print(hardware_report_dict)
