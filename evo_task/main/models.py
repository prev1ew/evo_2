from django.db import models


class Persons(models.Model):
    name = models.CharField('Имя', max_length=250, unique=True)
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.name}/{self.date}'

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'