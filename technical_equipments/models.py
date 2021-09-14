from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations
from jsonfield import JSONField


class TechnicalEquipments(BaseDictionaryModelAbstract):
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

    def get_module_id_by_signal_input_reg(self, signal_address):
        NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        module_id = None
        modules_in_plc = ModuleInPLC.objects.all()

        for module in modules_in_plc:
            address_number = []
            address_type = []
            for address in module.reference_address:
                # print(address['address'])
                for letter in address['address']:
                    address_list = []
                    if letter not in NUMBERS and letter != '0':
                        address_type.append(letter)
                    else:
                        address_number.append(letter)
                for i in range(int(address['length'])):
                    number = int(''.join(address_number))
                    number = number + i
                    address_final = ''.join(address_type) + '0' * (5 - len(str(number))) + str(number)
                    address_list.append(address_final)

                if signal_address in address_list:
                    module_id = module.id
                    # print(module.id)
                # print(address_list)

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
