# Generated by Django 3.2.7 on 2021-11-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0022_alter_header_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='advance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='cashRefund',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='grossBalance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='netBalance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pidbill',
            name='advance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pidbill',
            name='cashRefund',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pidbill',
            name='grossBalance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pidbill',
            name='netBalance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]