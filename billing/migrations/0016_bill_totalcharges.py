# Generated by Django 3.2.4 on 2021-09-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0015_bill_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='totalCharges',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
