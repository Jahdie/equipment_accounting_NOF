# Generated by Django 3.2.6 on 2021-09-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20210828_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compartments',
            old_name='photo_location',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='productions',
            old_name='photo_location',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='workshops',
            old_name='photo_location',
            new_name='photo',
        ),
    ]