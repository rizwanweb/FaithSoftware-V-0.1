# Generated by Django 3.2.4 on 2021-08-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20210812_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='addCustomDuty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='customDuty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='dutyType',
            field=models.CharField(choices=[('%', '%'), ('F', 'F')], max_length=5),
        ),
        migrations.AlterField(
            model_name='job',
            name='dv',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='exRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='excise',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='importValue',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='importValueUSD',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='incomeTax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='landingCharges',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='lcDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='pkr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='rateOfAddDuty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='rateOfDuty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='rateOfIT',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='rateOfST',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='salesTax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='terminalCharges',
            field=models.FloatField(),
        ),
    ]
