# Generated by Django 4.1 on 2022-08-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_app', '0004_alter_workorder_date_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='date_out',
            field=models.DateTimeField(),
        ),
    ]
