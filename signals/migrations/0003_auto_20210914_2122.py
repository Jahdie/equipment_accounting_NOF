# Generated by Django 3.2.6 on 2021-09-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0002_auto_20210904_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='signals',
            name='input_reg',
            field=models.CharField(max_length=15, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='signals',
            name='marking',
            field=models.CharField(max_length=15, null=True, verbose_name='Маркировка'),
        ),
    ]
