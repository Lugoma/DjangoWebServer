# Generated by Django 4.0.2 on 2022-04-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_paciente_edad_paciente_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_video', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='historico_camara',
            name='camara',
        ),
        migrations.RemoveField(
            model_name='historico_sensor',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='item',
            name='catalogo',
        ),
        migrations.RemoveField(
            model_name='paciente_persona',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='paciente_persona',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='tipo_persona',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='alarma',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='topic',
        ),
        migrations.AlterField(
            model_name='camara',
            name='tipo_camara',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='tipo_sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.topic'),
        ),
        migrations.DeleteModel(
            name='Catalogo',
        ),
        migrations.DeleteModel(
            name='Historico_Camara',
        ),
        migrations.DeleteModel(
            name='Historico_Sensor',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Paciente_Persona',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='video',
            name='camara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='api.camara'),
        ),
    ]
