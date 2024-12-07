from django.db import models
from django.contrib.gis.db import models as gis_models


class Camera(gis_models.Model):
    UPLOAD_TO = 'local_video'

    # point = gis_models.PointField(verbose_name='Позиция на карте')
    direction_text = models.CharField('Направление', max_length=50)
    local_video = models.FileField('Локальное видео', upload_to=UPLOAD_TO)
    problem_place = models.ForeignKey('map_traffic.Problem', on_delete=models.CASCADE, related_name='cameras')

    def __str__(self):
        return self.direction_text

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'


class Problem(gis_models.Model):
    # point = gis_models.PointField(verbose_name='Позиция на карте')
    name = models.CharField('Название', max_length=50)
    map_link = models.URLField('Ссылка на карту', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проблемное место'
        verbose_name_plural = 'Проблемные места'


class Claim(gis_models.Model):
    UPLOAD_TO = 'claim_photo'

    point = gis_models.PointField('Позиция на карте')
    description = models.TextField('Описание проблемы')
    phone = models.IntegerField('Номер телефона')
    photo = models.FileField('Фотография события', upload_to=UPLOAD_TO)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
