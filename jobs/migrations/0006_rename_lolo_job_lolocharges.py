# Generated by Django 3.2.6 on 2021-08-12 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_terminalcharges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='lolo',
            new_name='loloCharges',
        ),
    ]
