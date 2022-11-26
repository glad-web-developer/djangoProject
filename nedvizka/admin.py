from django.contrib import admin

from nedvizka.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fio',
        'data_rozdenia',
        'gorod'
    ]


    search_fields = [
        'id',
        'fio',
        'data_rozdenia',
        'gorod'
    ]

    list_filter = [
        'gorod'
    ]

    ordering = [
        'fio'
    ]

    list_editable = [
        'fio'
    ]

    save_as = True
    save_on_top = True


admin.site.register(Client, ClientAdmin)
