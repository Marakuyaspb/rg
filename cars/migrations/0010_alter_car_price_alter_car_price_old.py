# Generated by Django 5.1.1 on 2024-10-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_price_alter_car_price_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price_old',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена БЕЗ скидки'),
        ),
    ]
