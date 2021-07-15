from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from stations.models import ModuleInStations
from factory_equipments.models import EquipmentNames, EquipmentTypes


class SignalTypes(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Тип сигнала'
        verbose_name_plural = 'Типы сигналов'


class Signals(BaseDictionaryModelAbstract):
    marking = models.CharField(max_length=15, verbose_name='Маркировка')
    signal_type = models.ForeignKey('SignalTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип сигнала')
    module = models.ForeignKey('stations.ModuleInStations', on_delete=models.PROTECT, null=True,
                               verbose_name='Модуль в станции')
    equipment_type = models.ForeignKey('factory_equipments.EquipmentTypes', on_delete=models.PROTECT, null=True,
                                       verbose_name='Тип оборудования')
    equipment_name = models.ForeignKey('factory_equipments.EquipmentNames', on_delete=models.PROTECT, null=True,
                                       verbose_name='Наименование оборудования')

    class Meta:
        verbose_name = 'Сигнал'
        verbose_name_plural = 'Сигналы'
