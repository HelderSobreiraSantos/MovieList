# Generated by Django 5.0.7 on 2024-07-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0003_rename_duração_filme_duracao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
    ]
