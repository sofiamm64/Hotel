# Generated by Django 5.0.6 on 2024-06-25 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('Documento_C', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=25)),
                ('Apellido', models.CharField(max_length=25)),
                ('celular', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=30)),
                ('genero', models.CharField(max_length=1)),
                ('f_Nacimiento', models.DateTimeField()),
            ],
        ),
    ]