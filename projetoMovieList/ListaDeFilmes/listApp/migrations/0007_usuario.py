# Generated by Django 5.0.2 on 2024-09-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0006_alter_filme_generos_alter_filme_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
