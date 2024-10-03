from django.db import models

class Category(models.Model):
	id_cat = models.AutoField(primary_key=True)
	category = models.CharField(max_length=60, verbose_name='Категория')
	class Meta:
		ordering = ['category']
		indexes = [
			models.Index(fields=['category']),
		]
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'	

	def __str__(self):
		return self.category


class Status(models.Model):
	id_st = models.AutoField(primary_key=True)
	status = models.CharField(max_length=60, verbose_name='Новая / С пробегом')
	class Meta:
		ordering = ['status']
		indexes = [
			models.Index(fields=['status']),
		]
		verbose_name = 'Новая / С пробегом'
		verbose_name_plural = 'Новая / С пробегом'	

	def __str__(self):
		return self.status




class Car(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	status = models.ForeignKey(Status,
		related_name='statuses',
		on_delete=models.CASCADE, verbose_name = 'Новая/Уже нет')

	name = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Название модели')
	price = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Цена')
	price_old = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Цена БЕЗ скидки')
	year = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Год выпуска')
	engine = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Двигатель, л/с')
	mileage = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Пробег')
	transmission = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Трансмиссия')
	drive = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Привод')

	main_img = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото главное')
	img_1 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 1')
	img_2 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 2')
	img_3 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 3')
	img_4 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 4')
	img_5 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 5')
	img_6 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 6')
	img_7 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 7')
	img_8 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 8')
	img_9 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 9')
	img_10 = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name = 'Фото 10')

	available = models.BooleanField(default=True)

	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['id', 'name']),
		]
		verbose_name = 'Авто'
		verbose_name_plural = 'Авто'


# Order call form

class CallMe(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Запрос звонка'
		verbose_name_plural = 'Запросы звонков'


class CarSurvey_Full(models.Model):
	id = models.AutoField(primary_key=True)
	car_characteristics =  models.CharField(max_length=300, verbose_name = 'Марка, модель, мотор', null=True, blank=True)
	country = models.CharField(max_length=300, verbose_name = 'Из какой страны Вас интересует автомобиль?', null=True, blank=True)
	when =  models.CharField(max_length=300, verbose_name = 'Когда планируете покупать? ', null=True, blank=True)
	payment_type =  models.CharField(max_length=300, verbose_name = 'Форма оплаты за автомобиль? ', null=True, blank=True)
	max_price =  models.CharField(max_length=300, verbose_name = 'Максимальный бюджет для покупки?', null=True, blank=True)
	trade_in =  models.CharField(max_length=300, verbose_name = 'Планируете трейд ин? Какой авто? Пробег? ', null=True, blank=True)
	complectation =  models.CharField(max_length=600, verbose_name = 'Комплектация? ', null=True, blank=True)
	colors =  models.CharField(max_length=300, verbose_name = 'Желаемые цвета кузова и салона', null=True, blank=True)
	need_casco=  models.CharField(max_length=300, verbose_name = 'Планируете ли делать Каско', null=True, blank=True)
	real_price =  models.CharField(max_length=300, verbose_name = 'Какова стоимость реального предложения автомобиля, которое Вам удалось найти?', null=True, blank=True)

	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заказ машины: подробный опросник'
		verbose_name_plural = 'Заказ машины: подробный опросник'