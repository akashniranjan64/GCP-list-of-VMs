# Generated by Django 4.2 on 2023-04-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('vm_name', models.CharField(max_length=255)),
                ('vm_schedule_temp', models.CharField(max_length=255)),
                ('vm_sch_start', models.TimeField()),
                ('vm_sch_stop', models.TimeField()),
                ('vm_status', models.BooleanField()),
            ],
        ),
    ]
