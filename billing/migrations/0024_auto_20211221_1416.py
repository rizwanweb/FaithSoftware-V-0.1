# Generated by Django 3.2.7 on 2021-12-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0023_auto_20211127_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
