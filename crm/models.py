from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.defaultfilters import safe


class Otdel(models.Model):
    nazvanie = models.CharField('Название', max_length=255, null=False, blank=False, unique=True)
    korotkoye_nazvanie = models.CharField('Короткое имя', max_length=255, null=True, blank=True )
    adres_otdela = models.CharField('Адрес', max_length=255, null=True, blank=True )

    def get_kolvo_sotrudnikov(self):
        return self.sotrudnic_set.all().count()

    def __str__(self):
        return self.nazvanie

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

POL_LIST = ((1, 'Мужской'),(2,'Женский'))

class Sotrudnic(models.Model):
    fio = models.CharField('ФИО', max_length=255, null=False, blank=False, db_index=True)
    data_rozdenia = models.DateField('Дата рождения', null=False, blank=False, db_index=True)
    dolznost = models.CharField('Должность', max_length=255, null=False, blank=False, db_index=True)
    otdel = models.ForeignKey(Otdel, verbose_name='Отдел', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    email = models.EmailField('Почта', max_length=255, null=True,blank=True, db_index=True)
    telephone = models.CharField('Телефон', max_length=255, null=True,blank=True, db_index=True)
    pol = models.IntegerField('Пол',default=1, choices=POL_LIST, null=True,blank=True, db_index=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    adres_prozivania = models.CharField('Адрес проживания',  max_length=255, null=True,blank=True, db_index=True)
    photo = models.ImageField('Фото', null=True, blank=True, db_index=True)
    inn = models.CharField('ИНН', max_length=255, null=True,blank=True, db_index=True)
    passport_seria_nomer = models.CharField('Паспорт Серия и номер', max_length=255, null=True,blank=True, db_index=True)
    passport_vidan_kem_i_gde = models.CharField('Паспорт выдан когда и где', max_length=255, null=True,blank=True, db_index=True)

    def get_photo_admin(self):
        if self.photo:
            return safe(
                f'<a target="_black" href="{self.photo.url}"><img width=70 height=70 src="{self.photo.url}"></a>')
        return 'Нет'

    get_photo_admin.short_description = 'Фото'
    get_photo_admin.allow_tags = True


    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

class TipTehniki(models.Model):
    nazvanie = models.CharField('Название', max_length=255, null=False,blank=False)

    def __str__(self):
        return self.nazvanie

    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = 'Типы техники'

class OperazionaSistema(models.Model):
    nazvanie = models.CharField('Название', max_length=255, null=False,blank=False)

    def __str__(self):
        return self.nazvanie

    class Meta:
        verbose_name = 'Название Операционной системы'
        verbose_name_plural = 'Название Операционных систем'

class Otvetstveniy_sotrudnic(models.Model):
    fio = models.CharField('ФИО', max_length=255, null=False,blank=False)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Ответственный сотрудник'
        verbose_name_plural = 'Ответственные сотрудники'

class Tehnika(models.Model):
    nazvanie =models.CharField('Название', max_length=255)
    opisanie =models.TextField('Описание', null=True, blank=True)
    tip = models.ForeignKey(TipTehniki, verbose_name='Тип устройства', on_delete=models.SET_NULL, null=True,blank=True)
    inventarni_nomer = models.CharField('Инвентарный номер', max_length=255 , null=True, blank=True)
    operaziona_sistema = models.ForeignKey(OperazionaSistema, verbose_name='Операционная система', on_delete=models.SET_NULL, null=True, blank=True)
    otvestveni_sotrudnic = models.ForeignKey(Otvetstveniy_sotrudnic, verbose_name='Ответсвенный человек', null=True, blank=True, on_delete=models.SET_NULL)
    data_poslednie_proverki = models.DateField('Дата последней проверки', null=True, blank=True)


    def __str__(self):
        return self.nazvanie

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'