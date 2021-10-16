# Generated by Django 3.2.6 on 2021-08-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControllerFamilies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Семейство контроллеров',
                'verbose_name_plural': 'Семейства контроллеров',
            },
        ),
        migrations.CreateModel(
            name='ModuleTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Тип модуля',
                'verbose_name_plural': 'Типы модулей',
            },
        ),
        migrations.CreateModel(
            name='RackModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Модель Rack',
                'verbose_name_plural': 'Модели Rack',
            },
        ),
        migrations.CreateModel(
            name='TechnicalEquipmentTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Тип устройства',
                'verbose_name_plural': 'Типы устройств',
            },
        ),
        migrations.CreateModel(
            name='TechnicalEquipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('ip', models.CharField(max_length=15, null=True, verbose_name='IP адресс')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.locations', verbose_name='Местоположение')),
                ('technical_equipment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='technical_equipments.technicalequipmenttypes', verbose_name='Тип устройства')),
            ],
            options={
                'verbose_name': 'Техническое средство',
                'verbose_name_plural': 'Технические устройства',
            },
        ),
        migrations.CreateModel(
            name='ModuleModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('module_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='technical_equipments.moduletypes', verbose_name='Тип модуля')),
            ],
            options={
                'verbose_name': 'Модель модуля',
                'verbose_name_plural': 'Модели модулей',
            },
        ),
        migrations.CreateModel(
            name='ModuleInPLC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('rack', models.IntegerField(blank=True, verbose_name='Номер Rack')),
                ('slot', models.IntegerField(blank=True, verbose_name='Номер Slot')),
                ('module_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='technical_equipments.modulemodels', verbose_name='Модель модуля')),
                ('plc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='technical_equipments.technicalequipments', verbose_name='ПЛК')),
                ('rack_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='technical_equipments.rackmodels', verbose_name='Модель Rack')),
            ],
            options={
                'verbose_name': 'Модуль в станции',
                'verbose_name_plural': 'Модули в станциях',
            },
        ),
    ]
