# Generated by Django 5.1.4 on 2024-12-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_traffic', '0006_remove_camera_map_link_problem_map_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='map_link',
            field=models.URLField(max_length=300, verbose_name='Ссылка на карту'),
        ),
    ]
