# Generated by Django 3.2.4 on 2021-07-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stations', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwitchCabinets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.locations', verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'Коммутационный шкаф',
                'verbose_name_plural': 'Коммутационные шкафы',
            },
        ),
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адресс')),
            ],
            options={
                'verbose_name': 'Свитч',
                'verbose_name_plural': 'Свитчи',
            },
        ),
        migrations.CreateModel(
            name='SwitchModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('photo_location', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('ports_num', models.PositiveIntegerField(verbose_name='Количество портов')),
            ],
            options={
                'verbose_name': 'Модель свитча',
                'verbose_name_plural': 'Модели свитчей',
            },
        ),
        migrations.CreateModel(
            name='SwitchPorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('port_num', models.PositiveIntegerField(verbose_name='Номер порта')),
                ('is_trunc', models.BinaryField(verbose_name='Транк или хост')),
                ('station_or_port', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stations.stations', verbose_name='Станция или порт свитча')),
                ('switch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='switch_cabinets.switches', verbose_name='Свитч')),
            ],
            options={
                'verbose_name': 'Порт свитча',
                'verbose_name_plural': 'Порты свитчей',
            },
        ),
        migrations.AddField(
            model_name='switches',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='switch_cabinets.switchmodels', verbose_name='Модель свитча'),
        ),
        migrations.AddField(
            model_name='switches',
            name='switch_cabinet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='switch_cabinets.switchcabinets', verbose_name='Коммутационный шкаф'),
        ),
    ]
