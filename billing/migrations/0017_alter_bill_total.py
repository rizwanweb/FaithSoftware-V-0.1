# Generated by Django 3.2.7 on 2021-09-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_bill_totalcharges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(),
        ),
    ]
