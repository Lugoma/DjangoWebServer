# Generated by Django 4.0.2 on 2022-05-10 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_video_remove_historico_camara_camara_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='incubadora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to='api.incubadora'),
        ),
    ]
