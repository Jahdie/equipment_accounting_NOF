from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from django.db import models
from locations.models import Locations


class EquipmentTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class EquipmentNames(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = 'Наименования оборудования'


class EquipmentModels(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Модель оборудования'
        verbose_name_plural = 'Модели оборудования'


class AutomationComplex(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Комплекс автоматизации'
        verbose_name_plural = 'Комплексы автоматизации'


class DeviceName(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Имя устройства'
        verbose_name_plural = 'Имена устройств'


class Equipments(BaseModelAbstract):
    equipment_name = models.ForeignKey('EquipmentNames', on_delete=models.SET_NULL, null=True,
                                       verbose_name='Имя оборудования')
    equipment_type = models.ForeignKey('EquipmentTypes', on_delete=models.SET_NULL, null=True,
                                       verbose_name='Тип оборудования')
    equipment_model = models.ForeignKey('EquipmentModels', on_delete=models.SET_NULL, null=True,
                                        verbose_name='Модель оборудования')
    automation_complex = models.ForeignKey('AutomationComplex', on_delete=models.SET_NULL, null=True,
                                           verbose_name='Комплекс автоматизации')

    class Meta:
        verbose_name = 'Обоорудование'
        verbose_name_plural = 'Оборудование'
