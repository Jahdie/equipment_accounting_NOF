from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations


class ModuleInPLC(BaseModelAbstract):
    rack = models.IntegerField(blank=True, verbose_name='Номер Rack')
    slot = models.IntegerField(blank=True, verbose_name='Номер Slot')
    controller_family = models.ForeignKey('ControllerFamilies', on_delete=models.PROTECT, null=True,
                                          verbose_name='Семейство контроллеров')
    module_type = models.ForeignKey('ModuleTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип модуля')
    module_model = models.ForeignKey('ModuleModels', on_delete=models.PROTECT, null=True, verbose_name='Модель модуля')
    rack_model = models.ForeignKey('RackModels', on_delete=models.PROTECT, null=True, verbose_name='Модель Rack')
    plc = models.ForeignKey('PLC', on_delete=models.PROTECT, null=True,
                            verbose_name='Наименование PLC')

    class Meta:
        verbose_name = 'Модуль в станции'
        verbose_name_plural = 'Модули в станциях'


class PLC(BaseDictionaryModelAbstract):
    ip = models.CharField(max_length=15, verbose_name='IP адресс')
    location = models.ForeignKey('locations.Locations', on_delete=models.PROTECT, null=True,
                                 verbose_name='Местоположение')

    class Meta:
        verbose_name = 'ПЛК'
        verbose_name_plural = 'ПЛК'


class ControllerFamilies(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Семейство контроллеров'
        verbose_name_plural = 'Семейства контроллеров'


class ModuleModels(BaseDictionaryModelAbstract):

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
