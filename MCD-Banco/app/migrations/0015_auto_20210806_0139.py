# Generated by Django 2.2.24 on 2021-08-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210806_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='monto_pago',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]