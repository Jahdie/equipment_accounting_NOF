from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from django.db import models
from locations.models import Locations


class EquipmentTypes(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class DeviceTypes(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'


class EquipmentNames(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = 'Наименования оборудования'


class AutomationComplex(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Комплекс автоматизации'
        verbose_name_plural = 'Комплексы автоматизации'


class Equipments(BaseModelAbstract):
    equipment_name = models.ForeignKey('EquipmentNames', on_delete=models.SET_NULL, null=True,
                                       verbose_name='Имя оборудования')
    equipment_type = models.ForeignKey('EquipmentTypes', on_delete=models.SET_NULL, null=True,
                                       verbose_name='Тип оборудования')
    automation_complex = models.ForeignKey('AutomationComplex', on_delete=models.SET_NULL, null=True,
                                           verbose_name='Комплекс автоматизации')
    device_type = models.ForeignKey('DeviceTypes', on_delete=models.SET_NULL, null=True,
                                    verbose_name='Тип устройства')
    plc_name = models.ForeignKey('plc.PLC', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('locations.Locations', on_delete=models.PROTECT, null=True,
                                 verbose_name='Местоположение')

    class Meta:
        verbose_name = 'Обоорудование'
        verbose_name_plural = 'Оборудование'
