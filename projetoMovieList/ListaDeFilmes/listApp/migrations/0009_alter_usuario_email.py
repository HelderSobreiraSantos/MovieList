# Generated by Django 5.0.2 on 2024-09-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0008_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
