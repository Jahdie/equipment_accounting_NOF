from equipment_accounting_NOF.models import BaseModelAbstract, BaseDictionaryModelAbstract


class EquipmentTypes(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class EquipmentNames(BaseDictionaryModelAbstract):

    class Meta:
        verbose_name = 'Наименование оборудования'
        verbose_name_plural = 'Наименования оборудования'

