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
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True)
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    @staticmethod
    def get_locations_hierarchy():
        """Получаем иерархию локаций"""
        locations_dict_list = []
        for production in Locations.objects.distinct('production'):
            workshop_dicts_list = []
            locations_dict = {}
            locations_dict.update(
                {'production_name': production.production.name, 'production_id': production.production.id})
            locations_dict_list.append(locations_dict)

            for workshop in Locations.objects.filter(production_id=production.production_id).distinct('workshop_id'):
                compartments_dict_list = []
                workshops_dict = {}
                workshops_dict.update(
                    {'workshop_name': workshop.workshop.name, 'workshop_id': workshop.workshop.id})
                workshop_dicts_list.append(workshops_dict)
                locations_dict.update({'workshops': workshop_dicts_list})

                for compartment in Locations.objects.filter(production=workshop.production.id,
                                                            workshop=workshop.workshop.id):
                    compartments_dict = {}
                    compartments_dict.update(
                        {'compartment_name': compartment.compartment.name,
                         'compartment_id': compartment.compartment.id})
                    compartments_dict_list.append(compartments_dict)
                    workshops_dict.update({'compartments': compartments_dict_list})

        return locations_dict_list

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудования'
