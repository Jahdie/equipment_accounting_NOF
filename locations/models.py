from django.db import models
from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract


class Productions(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


class Workshops(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class Compartments(BaseDictionaryModelAbstract):
    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class Locations(BaseModelAbstract):
    production = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                   related_name='Productions')
    workshop = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудования'
