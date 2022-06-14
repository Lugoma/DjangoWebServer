# Generated by Django 4.0.2 on 2022-02-17 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_historico_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido1', models.CharField(blank=True, default='', max_length=200)),
                ('apellido2', models.CharField(blank=True, default='', max_length=200)),
                ('tipo_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='api.item')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='apellido1',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='paciente',
            name='apellido2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='api.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_persona', to='api.paciente')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_persona', to='api.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite_superior', models.IntegerField()),
                ('limite_inferior', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarmas', to='api.sensor')),
            ],
        ),
    ]
