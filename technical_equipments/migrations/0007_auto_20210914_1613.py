# Generated by Django 3.2.6 on 2021-09-14 09:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('technical_equipments', '0006_auto_20210914_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduleinplc',
            name='length_address',
        ),
        migrations.AlterField(
            model_name='moduleinplc',
            name='reference_address',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True, verbose_name='Адрес'),
        ),
    ]
