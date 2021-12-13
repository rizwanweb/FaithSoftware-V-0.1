# Generated by Django 3.2.7 on 2021-10-12 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20210916_1616'),
        ('refund', '0003_auto_20210927_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrefund',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AddField(
            model_name='jobrefund',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pidrefund',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AddField(
            model_name='pidrefund',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
