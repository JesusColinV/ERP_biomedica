# Generated by Django 4.1 on 2022-09-03 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('description', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('equipo', models.CharField(max_length=20)),
                ('evaluacion', models.CharField(max_length=20)),
                ('initial_state', models.CharField(max_length=20)),
                ('final_state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('reporta', models.CharField(max_length=20)),
                ('atiende', models.CharField(max_length=20)),
                ('reponsable', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Salidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=20)),
                ('provedor', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]
