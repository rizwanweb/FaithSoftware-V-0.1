# Generated by Django 3.2.7 on 2021-09-16 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20210916_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lolo',
            old_name='name',
            new_name='loloname',
        ),
    ]
