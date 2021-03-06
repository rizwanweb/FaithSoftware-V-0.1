# Generated by Django 3.2.7 on 2021-09-16 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_shippingline_options'),
        ('client', '0003_alter_client_options'),
        ('jobs', '0017_job_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PIDNo', models.IntegerField(unique=True)),
                ('jobDate', models.DateField()),
                ('containers', models.IntegerField(blank=True, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('packages', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('vessel', models.CharField(max_length=200)),
                ('igm', models.IntegerField()),
                ('igmDate', models.DateField()),
                ('index', models.IntegerField()),
                ('lc', models.CharField(blank=True, max_length=200, null=True)),
                ('lcDate', models.DateField(blank=True, null=True)),
                ('bl', models.CharField(max_length=200)),
                ('blDate', models.DateField(blank=True, null=True)),
                ('dv', models.FloatField()),
                ('quantity', models.FloatField()),
                ('exRate', models.FloatField()),
                ('importValueUSD', models.FloatField()),
                ('pkr', models.IntegerField()),
                ('insurance', models.IntegerField(blank=True, null=True)),
                ('landingCharges', models.IntegerField()),
                ('importValue', models.IntegerField()),
                ('dutyType', models.CharField(blank=True, choices=[('%', '%'), ('F', 'F')], max_length=5, null=True)),
                ('rateOfDuty', models.FloatField(blank=True, null=True)),
                ('customDuty', models.IntegerField(blank=True, null=True)),
                ('rateOfAddDuty', models.FloatField(blank=True, null=True)),
                ('addCustomDuty', models.IntegerField(blank=True, null=True)),
                ('rateOfST', models.FloatField(blank=True, null=True)),
                ('salesTax', models.IntegerField(blank=True, null=True)),
                ('rateOfIT', models.FloatField(blank=True, null=True)),
                ('incomeTax', models.IntegerField(blank=True, null=True)),
                ('rateOfCess', models.FloatField(blank=True, null=True)),
                ('cess', models.IntegerField(blank=True, null=True)),
                ('rateOfRD', models.FloatField(blank=True, null=True)),
                ('rd', models.IntegerField(blank=True, null=True)),
                ('rateOfAD', models.FloatField(blank=True, null=True)),
                ('antiDumping', models.IntegerField(blank=True, null=True)),
                ('excise', models.IntegerField(blank=True, null=True)),
                ('terminalCharges', models.IntegerField(blank=True, null=True)),
                ('do', models.IntegerField(blank=True, null=True)),
                ('deposit', models.IntegerField(blank=True, null=True)),
                ('loloCharges', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField()),
                ('billed', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item')),
                ('lolo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.lolo')),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.shippingline')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.terminal')),
            ],
        ),
    ]
