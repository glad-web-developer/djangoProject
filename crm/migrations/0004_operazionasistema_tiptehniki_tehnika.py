# Generated by Django 4.1.3 on 2022-11-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_nazvane_otdel_nazvanie'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperazionaSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'ОС',
                'verbose_name_plural': 'ОС',
            },
        ),
        migrations.CreateModel(
            name='TipTehniki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип техники',
                'verbose_name_plural': 'Типы техники',
            },
        ),
        migrations.CreateModel(
            name='Tehnika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=255, verbose_name='Название')),
                ('opisanie', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('inventarni_nomer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Инвентарный номер')),
                ('data_poslednie_proverki', models.DateField(blank=True, null=True, verbose_name='Дата последней проверки')),
                ('operaziona_sistema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.operazionasistema', verbose_name='ОС')),
                ('otvestveni_sotrudnic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.sotrudnic', verbose_name='Отвественный')),
                ('tip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.tiptehniki', verbose_name='Тип устройства')),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техники',
            },
        ),
    ]