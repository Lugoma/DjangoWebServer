# Generated by Django 4.0.2 on 2022-05-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_paciente_incubadora'),
    ]

    operations = [
        migrations.AddField(
            model_name='camara',
            name='puerto',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
