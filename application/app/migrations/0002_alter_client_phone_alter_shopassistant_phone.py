# Generated by Django 5.0 on 2023-12-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='shopassistant',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
    ]