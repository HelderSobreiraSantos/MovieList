# Generated by Django 5.0.7 on 2024-07-26 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0004_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listApp.genero'),
        ),
    ]
