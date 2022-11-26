from django.contrib import admin

# Register your models here.
from crm.models import Sotrudnic
from crm.models import Otdel
from crm.models import TipTehniki
from crm.models import OperazionaSistema
from crm.models import Otvetstveniy_sotrudnic
from crm.models import Tehnika

@admin.register(Sotrudnic)
class SotrudnicAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fio',
        'data_rozdenia',
        'otdel',
        'dolznost',
        'telephone',
        'pol',
        'user',
        'adres_prozivania',
         'get_photo_admin'

    ]
    list_display_links =[
        'otdel',
        'dolznost',
        'data_rozdenia',
        'otdel',
        'dolznost',
        'telephone',

    ]
    search_fields = [
        'id',
        'fio',
        'user__username'

    ]
    list_filter = [
        'otdel',
        'pol'
    ]
    ordering = [
        'fio'
    ]
    autocomplete_fields = [
        'otdel',
    ]

    list_editable = [
        'fio'

    ]

    save_as = True
    save_on_top = True



@admin.register(Otdel)
class OtdelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'korotkoye_nazvanie',
        'adres_otdela'

    ]

    search_fields = [
        'id',
        'nazvanie',
        'adres_otdela'
    ]
    list_filter = [
        'nazvanie',
    ]

    save_as = True
    save_on_top = True

@admin.register(Tehnika)
class TehnikaAdmin(admin.ModelAdmin):


    list_display = [
        'id',
        'nazvanie',
        'opisanie',
        'tip',
        'inventarni_nomer',
        'operaziona_sistema',
        'otvestveni_sotrudnic',
        'data_poslednie_proverki',
    ]
    list_display_links = [
        'id'
    ]

    search_fields = [
        'id',
        'nazvanie',
        'tip',
    ]
    list_editable = [
        'nazvanie',
        'otvestveni_sotrudnic'
    ]

    save_as = True
    save_on_top = True

@admin.register(TipTehniki)
class TipTehnikiAdmin(admin.ModelAdmin):


    list_display = [
        'id',
        'nazvanie',
    ]
    list_display_links = [
        'id'
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    list_editable = [
        'nazvanie',
    ]

    save_as = True
    save_on_top = True

@admin.register(OperazionaSistema)
class OperazionaSistemaAdmin(admin.ModelAdmin):


    list_display = [
        'id',
        'nazvanie',
    ]
    list_display_links = [
        'id'
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    list_editable = [
        'nazvanie',
    ]

    save_as = True
    save_on_top = True

@admin.register(Otvetstveniy_sotrudnic)
class Otvetstveniy_sotrudnicAdmin(admin.ModelAdmin):


    list_display = [
        'id',
        'fio',
    ]
    list_display_links = [
        'id'
    ]
    search_fields = [
        'id',
        'fio',
    ]
    list_editable = [
        'fio',
    ]

    save_as = True
    save_on_top = True
