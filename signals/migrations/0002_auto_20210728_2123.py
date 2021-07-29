# Generated by Django 3.2.5 on 2021-07-28 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjustableParameters',
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
                'verbose_name': 'Регулируемый параметр',
                'verbose_name_plural': 'Регулируемые параметры',
            },
        ),
        migrations.AddField(
            model_name='signals',
            name='adjustable_parameter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='signals.adjustableparameters', verbose_name='Регулируемый параметр'),
        ),
    ]