from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from technical_equipments.models import ModuleInPLC
from factory_equipments.models import EquipmentNames, EquipmentTypes


class SignalTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип сигнала'
        verbose_name_plural = 'Типы сигналов'

    def __str__(self):
        return self.name


class AdjustableParameters(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Регулируемый параметр'
        verbose_name_plural = 'Регулируемые параметры'


class Signals(BaseDictionaryModelAbstract):
    marking = models.CharField(max_length=15, verbose_name='Маркировка')
    signal_type = models.ForeignKey('SignalTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип сигнала')
    adjustable_parameter = models.ForeignKey('AdjustableParameters', on_delete=models.PROTECT, null=True,
                                             verbose_name='Регулируемый параметр')
    module = models.ForeignKey('technical_equipments.ModuleInPLC', on_delete=models.PROTECT, null=True,
                               verbose_name='Модуль в станции')
    equipment = models.ForeignKey('factory_equipments.Equipments', on_delete=models.PROTECT, null=True,
                                  verbose_name='Оборудование')

    class Meta:
        verbose_name = 'Сигнал'
        verbose_name_plural = 'Сигналы'
