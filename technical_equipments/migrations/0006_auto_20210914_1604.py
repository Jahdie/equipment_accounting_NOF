# Generated by Django 3.2.6 on 2021-09-14 09:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technical_equipments', '0005_auto_20210914_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleinplc',
            name='length_address',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=None, null=True, size=None, verbose_name='Длинна адрессации'),
        ),
        migrations.AlterField(
            model_name='moduleinplc',
            name='reference_address',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=None, null=True, size=None, verbose_name='Адрес'),
        ),
    ]
