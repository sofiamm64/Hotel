# Generated by Django 5.0.6 on 2024-06-25 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('Codigo_S', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=25)),
                ('Precio', models.IntegerField()),
                ('Descripcion', models.TextField()),
            ],
        ),
    ]