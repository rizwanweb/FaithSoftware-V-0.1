# Generated by Django 3.2.6 on 2021-09-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20210906_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='containers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]