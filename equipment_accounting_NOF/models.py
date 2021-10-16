from django.db import models


class BaseModelAbstract(models.Model):
    note = models.TextField(blank=True, verbose_name='Примечание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class BaseDictionaryModelAbstract(BaseModelAbstract):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
