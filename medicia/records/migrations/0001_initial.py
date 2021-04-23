# Generated by Django 3.2 on 2021-04-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=16)),
                ('role', models.CharField(choices=[('doctor', 'Doctor'), ('pharmacist', 'Pharmacist'), ('nurse', 'Nurse'), ('paramedic', 'Paramedic'), ('non-medic', 'Non-medic')], default='doctor', max_length=100)),
                ('employed', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('_id',),
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('height', models.PositiveIntegerField(default=1)),
                ('weight', models.PositiveIntegerField(default=1)),
                ('genotype', models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('AC', 'AC'), ('SC', 'SC'), ('CC', 'CC')], max_length=2)),
                ('bg', models.CharField(choices=[('A+', 'A-positive'), ('A-', 'A-negative'), ('B+', 'B-positive'), ('B-', 'B-negative'), ('O+', 'O-positive'), ('O-', 'O-negative'), ('AB+', 'AB-positive'), ('AB-', 'AB-negative')], max_length=3)),
                ('gender', models.CharField(max_length=40)),
                ('allergies', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('_id',),
            },
        ),
    ]
