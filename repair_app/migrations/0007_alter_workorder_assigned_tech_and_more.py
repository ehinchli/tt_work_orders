# Generated by Django 4.1 on 2022-08-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_app', '0006_alter_workorder_date_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='assigned_tech',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='date_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='repair_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='tech_notes',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
