# Generated by Django 5.0.2 on 2024-03-08 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0002_filme_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='duração',
            new_name='duracao',
        ),
    ]
