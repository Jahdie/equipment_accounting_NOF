# Generated by Django 3.2.6 on 2021-09-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('switch_cabinets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switchcabinets',
            old_name='photo_location',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='switchmodels',
            old_name='photo_location',
            new_name='photo',
        ),
    ]
