# Generated by Django 4.2.5 on 2023-10-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_tareas', '0002_alter_tarea_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(),
        ),
    ]