# Generated by Django 2.2.24 on 2021-08-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210806_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='comision_ganada',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='comision',
            name='monto_colocado',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='credito',
            name='monto_otorgado',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='credito',
            name='monto_pago',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='monto_pagado',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
