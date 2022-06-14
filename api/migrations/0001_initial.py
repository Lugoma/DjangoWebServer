# Generated by Django 4.0.2 on 2022-02-17 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Incubadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('direccion_ip', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=False)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=False)),
                ('incubadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.incubadora')),
                ('tipo_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.item')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.PositiveIntegerField()),
                ('incubadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to='api.incubadora')),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Camara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_video', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('camara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_camaras', to='api.camara')),
            ],
        ),
        migrations.AddField(
            model_name='camara',
            name='incubadora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camaras', to='api.incubadora'),
        ),
        migrations.AddField(
            model_name='camara',
            name='tipo_camara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camaras', to='api.item'),
        ),
    ]
