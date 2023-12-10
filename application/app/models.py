from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class Client(models.Model):
    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"
        ordering = ["id"]

    first_name = models.CharField(max_length=60, unique=True, verbose_name="ФИО")
    description = models.CharField(max_length=1000, verbose_name="Описание")
    phone = models.CharField(
        max_length=50, verbose_name="Телефон"
    )

    def __str__(self):
        return self.first_name + " " + self.phone


class Brand(models.Model):
    class Meta:
        verbose_name = "Марки"
        verbose_name_plural = "Марки"
        ordering = ["id"]

    name = models.CharField(max_length=20, verbose_name="Марки")
    engine_type = models.CharField(max_length=20, verbose_name="Тип топлива")
    body_type = models.CharField(max_length=20, null=True, verbose_name="Тип кузова")


class CarShowroom(models.Model):
    class Meta:
        verbose_name = "Автосалон"
        verbose_name_plural = "Автосалоны"

    client_id = models.IntegerField(Client)
    sale_id = models.IntegerField(verbose_name="ID продажи")
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название автосалона"
    )
    rating = models.FloatField(verbose_name="Рейтинг")
    address = models.CharField(max_length=100, verbose_name="Адрес")

    def __str__(self):
        return self.name


class Automobile(models.Model):
    class Meta:
        verbose_name = "Автомобили"
        verbose_name_plural = "Автомобили"
        ordering = ["id"]

    id_car_showroom = models.IntegerField(CarShowroom)
    id_brand = models.IntegerField(Brand)
    rating = models.FloatField(verbose_name="Рейтинг")
    price = models.IntegerField(verbose_name="Цена")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    transmit_number = models.CharField(max_length=50, unique=True, verbose_name="VIN")

    def __str__(self):
        return str(self.transmit_number) + " " + str(self.id_brand)


class ShopAssistant(models.Model):
    class Meta:
        verbose_name = "Ассистенты"
        verbose_name_plural = "Ассистенты"
        ordering = ["id"]

    id_car_showroom = models.IntegerField(CarShowroom)
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя")
    phone = models.CharField(
        max_length=15, verbose_name="Телефон"
    )
    data_start = models.CharField(max_length=15, verbose_name="Приступил к работе с")
    sales_count = models.IntegerField(verbose_name="Кол-во продаж")

    def __str__(self):
        return self.name


class Sale(models.Model):
    class Meta:
        verbose_name = "Продажи"
        verbose_name_plural = "Продажи"
        ordering = ["id"]

    id_shop_assistant = models.IntegerField(ShopAssistant)
    automobile_id = models.IntegerField(verbose_name="ID Автомобиля")
    payment_type = models.CharField(max_length=30, verbose_name="Тип оплаты")
    data = models.DateField(verbose_name="Дата продажи")

    def __str__(self):
        return (
            str(self.data) + " " + self.payment_type + " " + str(self.id_shop_assistant)
        )
