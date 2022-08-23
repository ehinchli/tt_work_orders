# Generated by Django 4.1 on 2022-08-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netid', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('affiliation', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=200)),
                ('warranty_type', models.CharField(max_length=200)),
                ('misc_hardware', models.CharField(max_length=200)),
                ('data_backup', models.CharField(max_length=200)),
                ('find_my_mac', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_notes', models.CharField(max_length=2000)),
                ('tech_notes', models.CharField(max_length=2000)),
                ('assigned_tech', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('repair_cost', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair_app.client')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair_app.device')),
            ],
        ),
    ]
