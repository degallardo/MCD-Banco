# Generated by Django 2.2.24 on 2021-08-06 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_tarjetacredito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='region',
        ),
    ]
