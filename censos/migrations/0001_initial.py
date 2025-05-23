# Generated by Django 4.2.3 on 2025-05-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Censo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=20, null=True)),
                ('tiene_hijos', models.BooleanField(default=False)),
                ('cantidad_hijos', models.IntegerField(blank=True, null=True)),
                ('edades_hijos', models.TextField(blank=True, null=True)),
                ('nivel_educativo', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=100, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
