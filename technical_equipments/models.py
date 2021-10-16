from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations
from jsonfield import JSONField


class TechnicalEquipments(BaseDictionaryModelAbstract):
    project = models.CharField(max_length=150, verbose_name='IP адресс', null=True)
    ip = models.CharField(max_length=15, verbose_name='IP адресс', null=True)
    technical_equipment_type = models.ForeignKey('TechnicalEquipmentTypes', on_delete=models.PROTECT, null=True,
                                                 verbose_name='Тип устройства')
    location = models.ForeignKey('locations.Locations', on_delete=models.PROTECT, null=True,
                                 verbose_name='Местоположение')

    class Meta:
        verbose_name = 'Техническое средство'
        verbose_name_plural = 'Технические устройства'


class ModuleInPLC(BaseModelAbstract):
    rack = models.IntegerField(blank=True, verbose_name='Номер Rack')
    slot = models.IntegerField(blank=True, verbose_name='Номер Slot')
    module_type = models.ForeignKey('ModuleTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип модуля')
    module_model = models.ForeignKey('ModuleModels', on_delete=models.PROTECT, null=True, verbose_name='Модель модуля')
    rack_model = models.ForeignKey('RackModels', on_delete=models.PROTECT, null=True, verbose_name='Модель Rack')
    plc = models.ForeignKey('TechnicalEquipments', on_delete=models.PROTECT, null=True, verbose_name='ПЛК')
    reference_address = JSONField(null=True, blank=True, default=None, verbose_name='Адрес')

    @staticmethod
    def get_module_id_by_signal_input_reg(signal_address, project, plc_name):
        """Получаем ID модуля к коттруму приинадлежит адрес сигнала"""
        module_id = None
        # print(project, plc_name)
        if plc_name is not None:
            modules_in_plc = ModuleInPLC.objects.filter(plc__project=project, plc__name=plc_name)
            # print(modules_in_plc)
        else:
            modules_in_plc = ModuleInPLC.objects.filter(plc__project=project)
            # print(modules_in_plc)
        for module in modules_in_plc:
            # for address in module.reference_address:
            if not not module.reference_address:
                for address in module.reference_address:
                    # print(address)
                    address_numbers = []
                    address_type = []
                    signal_address_type = []
                    signal_address_numbers = []
                    for symbol in address['address']:
                        if symbol not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            address_type.append(symbol)
                        else:
                            address_numbers.append(symbol)
                    for symbol in signal_address:
                        if symbol not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            signal_address_type.append(symbol)
                        else:
                            signal_address_numbers.append(symbol)
                    if address_type == signal_address_type:
                        # print(address_type, signal_address_type)
                        first_address_in_range = int(''.join(address_numbers))
                        last_address_in_range = first_address_in_range + int(address['length'])
                        sought_address = int(''.join(signal_address_numbers))
                        if first_address_in_range <= sought_address <= last_address_in_range:
                            module_id = module.id
        return module_id

    class Meta:
        verbose_name = 'Модуль в станции'
        verbose_name_plural = 'Модули в станциях'


class ControllerFamilies(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Семейство контроллеров'
        verbose_name_plural = 'Семейства контроллеров'


class ModuleModels(BaseDictionaryModelAbstract):
    module_type = models.ForeignKey('ModuleTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип модуля')

    class Meta:
        verbose_name = 'Модель модуля'
        verbose_name_plural = 'Модели модулей'


class RackModels(BaseDictionaryModelAbstract):
    rack_type = models.ForeignKey('RackTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип Rack')

    class Meta:
        verbose_name = 'Модель Rack'
        verbose_name_plural = 'Модели Rack'


class RackTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип Rack'
        verbose_name_plural = 'Типы Rack'


class ModuleTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип модуля'
        verbose_name_plural = 'Типы модулей'


class TechnicalEquipmentTypes(BaseDictionaryModelAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'
