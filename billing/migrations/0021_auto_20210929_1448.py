# Generated by Django 3.2.7 on 2021-09-29 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0020_auto_20210929_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pidbill',
            options={'ordering': ['pidbillNo']},
        ),
        migrations.RenameField(
            model_name='pidbill',
            old_name='billNo',
            new_name='pidbillNo',
        ),
    ]