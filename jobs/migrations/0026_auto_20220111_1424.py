# Generated by Django 3.2.7 on 2022-01-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0025_auto_20211221_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='psqcTesting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='psqcaSDC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pid',
            name='psqcTesting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pid',
            name='psqcaSDC',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
