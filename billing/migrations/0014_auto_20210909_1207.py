# Generated by Django 3.2.4 on 2021-09-09 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0013_auto_20210909_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='billDate',
            field=models.DateField(default=datetime.date(2021, 9, 9)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='cashNoDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='gdNoDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
