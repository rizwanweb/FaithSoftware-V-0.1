# Generated by Django 3.2.7 on 2021-09-16 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pid',
            old_name='jobDate',
            new_name='Date',
        ),
    ]
