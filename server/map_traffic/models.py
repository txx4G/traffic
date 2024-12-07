from django.db import models
from django.contrib.gis.db import models as gis_models


class Camera(gis_models.Model):
    UPLOAD_TO = 'local_video'

    # point = gis_models.PointField(verbose_name='Позиция на карте')
    direction_text = models.CharField(max_length=50)
    local_video = models.FileField(upload_to=UPLOAD_TO)
    map_link = models.URLField('Ссылка на карту')

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'


class Problem(gis_models.Model):
    # point = gis_models.PointField(verbose_name='Позиция на карте')
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Проблемное место'
        verbose_name_plural = 'Проблемные места'
