# Generated by Django 3.2.5 on 2021-07-21 06:22

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
            name='ModuleModels',
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
                'verbose_name': 'Модель модуля',
                'verbose_name_plural': 'Модели модулей',
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
            name='Stations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адресс')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.locations', verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станции',
            },
        ),
        migrations.CreateModel(
            name='ModuleInStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('controller_family_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stations.controllerfamilies', verbose_name='Семейство контроллеров')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stations.modulemodels', verbose_name='Модель модуля')),
                ('module_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stations.moduletypes', verbose_name='Тип модуля')),
            ],
            options={
                'verbose_name': 'Модуль в станции',
                'verbose_name_plural': 'Модули в станциях',
            },
        ),
    ]
