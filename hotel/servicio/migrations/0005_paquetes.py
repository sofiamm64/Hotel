# Generated by Django 5.0.6 on 2024-06-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_habitacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='paquetes',
            fields=[
                ('Codigo_Pa', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Destinatario', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=25)),
                ('Fecha', models.DateTimeField()),
            ],
        ),
    ]