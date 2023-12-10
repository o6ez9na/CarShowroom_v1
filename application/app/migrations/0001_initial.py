# Generated by Django 5.0 on 2023-12-09 12:26

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car_showroom', models.IntegerField(verbose_name=app.models.CarShowroom)),
                ('id_brand', models.IntegerField(verbose_name=app.models.Brand)),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('transmit_number', models.CharField(max_length=50, unique=True, verbose_name='VIN')),
            ],
            options={
                'verbose_name': 'Автомобили',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Марки')),
                ('engine_type', models.CharField(max_length=20, verbose_name='Тип топлива')),
                ('body_type', models.CharField(max_length=20, null=True, verbose_name='Тип кузова')),
            ],
            options={
                'verbose_name': 'Марки',
                'verbose_name_plural': 'Марки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CarShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(verbose_name=app.models.Client)),
                ('sale_id', models.IntegerField(verbose_name='ID продажи')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название автосалона')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Автосалон',
                'verbose_name_plural': 'Автосалоны',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, unique=True, verbose_name='ФИО')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание')),
                ('phone', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Пример: 1. +79803228724', regex='^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')], verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_shop_assistant', models.IntegerField(verbose_name=app.models.ShopAssistant)),
                ('automobile_id', models.IntegerField(verbose_name='ID Автомобиля')),
                ('payment_type', models.CharField(max_length=30, verbose_name='Тип оплаты')),
                ('data', models.DateField(verbose_name='Дата продажи')),
            ],
            options={
                'verbose_name': 'Продажи',
                'verbose_name_plural': 'Продажи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ShopAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car_showroom', models.IntegerField(verbose_name=app.models.CarShowroom)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Пример: 1. +79803228724, 2. 89803228724', regex='^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')], verbose_name='Телефон')),
                ('data_start', models.CharField(max_length=15, verbose_name='Приступил к работе с')),
                ('sales_count', models.IntegerField(verbose_name='Кол-во продаж')),
            ],
            options={
                'verbose_name': 'Ассистенты',
                'verbose_name_plural': 'Ассистенты',
                'ordering': ['id'],
            },
        ),
    ]
