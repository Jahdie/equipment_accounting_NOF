from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract
from locations.models import Locations


class ModuleInStations(BaseModelAbstract):
    module_type = models.ForeignKey('ModuleTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип модуля')
    controller_family_id = models.ForeignKey('ControllerFamilies', on_delete=models.PROTECT, null=True,
                                             verbose_name='Семейство контроллеров')
    model = models.ForeignKey('ModuleModels', on_delete=models.PROTECT, null=True, verbose_name='Модель модуля')

    class Meta:
        verbose_name = 'Модуль в станции'
        verbose_name_plural = 'Модули в станциях'


class Stations(BaseDictionaryModelAbstract):
    ip = models.CharField(max_length=15, verbose_name='IP адресс')
    location = models.ForeignKey('locations.Locations', on_delete=models.PROTECT, null=True, verbose_name='Местоположение')

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class ControllerFamilies(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Семейство контроллеров'
        verbose_name_plural = 'Семейства контроллеров'


class ModuleModels(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Модель модуля'
        verbose_name_plural = 'Модели модулей'


class ModuleTypes(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Тип модуля'
        verbose_name_plural = 'Типы модулей'



