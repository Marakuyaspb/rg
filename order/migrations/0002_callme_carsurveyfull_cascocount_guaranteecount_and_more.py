# Generated by Django 5.1.1 on 2024-10-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallMe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка: перезвоните мне',
                'verbose_name_plural': 'Заявки: перезвоните мне',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CarSurveyFull',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_characteristics', models.CharField(blank=True, max_length=300, null=True, verbose_name='Марка, модель, мотор')),
                ('country', models.CharField(blank=True, max_length=300, null=True, verbose_name='Из какой страны Вас интересует автомобиль?')),
                ('when', models.CharField(blank=True, max_length=300, null=True, verbose_name='Когда планируете покупать? ')),
                ('payment_type', models.CharField(blank=True, max_length=300, null=True, verbose_name='Форма оплаты за автомобиль?')),
                ('max_price', models.CharField(blank=True, max_length=300, null=True, verbose_name='Максимальный бюджет для покупки?')),
                ('trade_in', models.CharField(blank=True, max_length=300, null=True, verbose_name='Планируете трейд ин? Какой авто? Пробег?')),
                ('complectation', models.CharField(blank=True, max_length=600, null=True, verbose_name='Комплектация?')),
                ('colors', models.CharField(blank=True, max_length=300, null=True, verbose_name='Желаемые цвета кузова и салона')),
                ('need_casco', models.BooleanField(default=True, verbose_name='Планируете ли делать Каско')),
                ('real_price', models.CharField(blank=True, max_length=300, null=True, verbose_name='Какова стоимость реального предложения автомобиля, которое Вам удалось найти?')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ машины: подробный опросник',
                'verbose_name_plural': 'Заказ машины: подробный опросник',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CascoCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('budget', models.CharField(default=True, max_length=30, verbose_name='Какой бюджет?')),
                ('type', models.CharField(blank=True, max_length=30, null=True, verbose_name='Дизель / электрокар?')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка на рассчет КАСКО',
                'verbose_name_plural': 'Заявки на рассчет КАСКО',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GuaranteeCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('who_sold', models.BooleanField(default=True, verbose_name='Авто куплено через R.E.D. Group?')),
                ('have_goverment_number', models.BooleanField(default=True, verbose_name='Есть ли Гос. номер?')),
                ('goverment_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Если да, укажите:')),
                ('is_gai_record', models.BooleanField(default=True, verbose_name='Поставлена ли машина на учёт?')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка на рассчет гарантии',
                'verbose_name_plural': 'Заявки на рассчет гарантии',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LegalHelp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('where_auto', models.CharField(blank=True, max_length=300, null=True, verbose_name='  Где сейчас находится авто? В РФ/в др.стране/на таможне?')),
                ('documents', models.CharField(blank=True, max_length=300, null=True, verbose_name=' Какие документы у вас есть сейчас?')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Запрос юридической поддержки',
                'verbose_name_plural': 'Запросы юридической поддержки',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NeedDiagnostic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('urgency', models.BooleanField(default=True, verbose_name='Срочно?')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка на диагностику',
                'verbose_name_plural': 'Заявки на диагностику',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NeedServece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('urgency', models.BooleanField(default=True, verbose_name='Срочно?')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка на сервисное обслуживание',
                'verbose_name_plural': 'Заявки на сервисное обслуживание',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ShesterenkyNeed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(blank=True, max_length=30, null=True, verbose_name='Год выпуска')),
                ('vin', models.CharField(blank=True, max_length=30, null=True, verbose_name='VIN-номер')),
                ('its_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название детали')),
                ('img', models.ImageField(blank=True, null=True, upload_to='spares/', verbose_name='Фото детали')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка на запчасть',
                'verbose_name_plural': 'Заявки на запчасти',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='WantThisCar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_id', models.CharField(max_length=30, verbose_name='Марка машины')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Хочу такую же',
                'verbose_name_plural': 'Запросы: хочу такую же!',
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='car',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
