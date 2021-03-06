# Generated by Django 3.2.7 on 2021-09-20 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0019_rename_jobdate_pid_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField()),
                ('damageCharges', models.IntegerField()),
                ('washingCharges', models.IntegerField()),
                ('refundAmount', models.IntegerField()),
                ('dueDate', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('jobNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
