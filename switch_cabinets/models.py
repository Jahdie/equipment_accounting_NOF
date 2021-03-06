from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations
from technical_equipments.models import TechnicalEquipments


class SwitchPorts(BaseModelAbstract):
    port_num = models.PositiveIntegerField(verbose_name='Номер порта')
    technical_equipment = models.ForeignKey('technical_equipments.TechnicalEquipments', on_delete=models.PROTECT,
                                            null=True, verbose_name='Устройство')
    switch = models.ForeignKey('Switches', on_delete=models.PROTECT, null=True, verbose_name='Свитч')

    class Meta:
        verbose_name = 'Порт свитча'
        verbose_name_plural = 'Порты свитчей'


class SwitchCabinets(BaseDictionaryModelAbstract):
    location = models.ForeignKey('locations.Locations', on_delete=models.PROTECT, null=True,
                                 verbose_name='Местоположение')

    class Meta:
        verbose_name = 'Коммутационный шкаф'
        verbose_name_plural = 'Коммутационные шкафы'


class SwitchModels(BaseDictionaryModelAbstract):
    ports_num = models.PositiveIntegerField(verbose_name='Количество портов', null=True)

    class Meta:
        verbose_name = 'Модель свитча'
        verbose_name_plural = 'Модели свитчей'


class Switches(BaseModelAbstract):
    ip = models.CharField(max_length=15, verbose_name='IP адресс')
    switch_cabinet = models.ForeignKey('SwitchCabinets', on_delete=models.PROTECT, null=True,
                                       verbose_name='Коммутационный шкаф')
    model = models.ForeignKey('SwitchModels', on_delete=models.PROTECT, null=True, verbose_name='Модель свитча')

    class Meta:
        verbose_name = 'Свитч'
        verbose_name_plural = 'Свитчи'
