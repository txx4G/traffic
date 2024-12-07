from django.db import models


class Employee(models.Model):
    name = models.CharField(max=100)
    role = models.CharField(max=50)

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'
