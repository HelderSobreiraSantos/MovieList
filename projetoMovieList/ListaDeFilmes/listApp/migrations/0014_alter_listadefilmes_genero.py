# Generated by Django 5.0.2 on 2024-09-22 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0013_listadefilmes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listadefilmes',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listApp.genero'),
        ),
    ]