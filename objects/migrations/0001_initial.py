# Generated by Django 4.1 on 2022-09-03 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('atentions', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('numero_contacto', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meta_device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=20)),
                ('fecha_adquisicion', models.DateTimeField(verbose_name='fecha en que se registró')),
                ('fecha_retiro', models.DateTimeField(verbose_name='fecha en que se retiró')),
                ('area_asignado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('dia', models.CharField(max_length=20)),
                ('inicio', models.CharField(max_length=20)),
                ('fin', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Device_extern',
            fields=[
                ('meta_device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.meta_device')),
                ('uses', models.SmallIntegerField(default=0)),
            ],
            bases=('objects.meta_device',),
        ),
        migrations.CreateModel(
            name='Device_intern',
            fields=[
                ('meta_device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.meta_device')),
                ('id_label', models.CharField(max_length=7, unique=True)),
                ('status', models.CharField(max_length=10)),
                ('maintenance', models.SmallIntegerField(default=0)),
                ('area_de_uso', models.CharField(max_length=20)),
            ],
            bases=('objects.meta_device',),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('contacto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.contacto')),
                ('Equipo', models.CharField(max_length=20)),
            ],
            bases=('objects.contacto',),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('contacto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.contacto')),
                ('Puesto', models.CharField(max_length=20)),
                ('Horario', models.CharField(max_length=20)),
            ],
            bases=('objects.contacto',),
        ),
    ]
