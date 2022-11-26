from django.db import models

# Create your models here.
class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    fio = models.CharField('ФИО', max_length=255)
    data_rozdenia = models.DateTimeField('Дата рождения')
    gorod = models.CharField('Город', max_length=255)

    def __str__(self):
        return self.fio