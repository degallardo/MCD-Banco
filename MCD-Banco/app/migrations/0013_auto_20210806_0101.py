# Generated by Django 2.2.24 on 2021-08-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210806_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudcredito',
            name='monto_solicitado',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]