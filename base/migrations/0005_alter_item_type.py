# Generated by Django 3.2.6 on 2021-08-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(blank=True, choices=[('EDIBLE', 'EDIBLE'), ('Tin Plate', 'Tin Plate'), ('Soap Noodles', 'Soap Noodles')], max_length=50, null=True),
        ),
    ]
