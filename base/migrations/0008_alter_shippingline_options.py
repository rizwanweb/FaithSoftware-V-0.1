# Generated by Django 3.2.6 on 2021-09-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_item_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingline',
            options={'ordering': ['name']},
        ),
    ]