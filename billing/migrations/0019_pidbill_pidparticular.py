# Generated by Django 3.2.7 on 2021-09-28 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20210916_1616'),
        ('jobs', '0019_rename_jobdate_pid_date'),
        ('billing', '0018_alter_bill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PIDParticular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('reciept', models.CharField(blank=True, max_length=150, null=True)),
                ('byUs', models.FloatField(blank=True, null=True)),
                ('byYou', models.FloatField(blank=True, null=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.pid')),
            ],
            options={
                'ordering': ['pid'],
            },
        ),
        migrations.CreateModel(
            name='PIDBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billNo', models.IntegerField()),
                ('billDate', models.DateField()),
                ('gdNo', models.CharField(blank=True, max_length=20, null=True)),
                ('gdNoDate', models.DateField(blank=True, null=True)),
                ('cashNo', models.CharField(blank=True, max_length=20, null=True)),
                ('cashNoDate', models.DateField(blank=True, null=True)),
                ('grossTotal', models.FloatField(blank=True, null=True)),
                ('charges', models.FloatField(blank=True, null=True)),
                ('rateOfST', models.FloatField(blank=True, null=True)),
                ('salesTax', models.FloatField(blank=True, null=True)),
                ('totalCharges', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField()),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('inwords', models.CharField(blank=True, max_length=500, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.pid')),
            ],
            options={
                'ordering': ['billNo'],
            },
        ),
    ]