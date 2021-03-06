# Generated by Django 4.0.2 on 2022-03-03 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_paciente_incubadora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camara',
            name='incubadora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='camaras', to='api.incubadora'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='incubadora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.incubadora'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.topic'),
        ),
    ]
