# Generated by Django 5.1.1 on 2024-12-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_delete_callmeitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cascocount',
            name='budget',
            field=models.CharField(max_length=30, verbose_name='Какой бюджет?'),
        ),
        migrations.AlterField(
            model_name='legalhelp',
            name='documents',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Какие документы у вас есть сейчас?'),
        ),
        migrations.AlterField(
            model_name='legalhelp',
            name='where_auto',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Где сейчас находится авто? В РФ/в др.стране/на таможне?'),
        ),
    ]
