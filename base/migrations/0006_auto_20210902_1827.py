# Generated by Django 3.2.4 on 2021-09-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lolo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingline',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='terminal',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
