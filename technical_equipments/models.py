from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations


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
    module_model = models.ForeignKey('ModuleModels', on_delete=models.PROTECT, null=True, verbose_name='Модель модуля')
    rack_model = models.ForeignKey('RackModels', on_delete=models.PROTECT, null=True, verbose_name='Модель Rack')
    plc = models.ForeignKey('TechnicalEquipments', on_delete=models.PROTECT, null=True, verbose_name='ПЛК')

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
    class Meta:
        verbose_name = 'Модель Rack'
        verbose_name_plural = 'Модели Rack'


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
