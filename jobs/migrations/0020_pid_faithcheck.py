# Generated by Django 3.2.7 on 2021-10-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_rename_jobdate_pid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pid',
            name='faithCheck',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]