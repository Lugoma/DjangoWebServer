# Generated by Django 4.0.2 on 2022-03-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_camara_incubadora_alter_sensor_incubadora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='tipo_sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensores', to='api.item'),
        ),
    ]
