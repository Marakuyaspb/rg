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


class Color(models.Model):
	color_id = models.AutoField(primary_key=True)
	color_name = models.CharField(max_length=50, verbose_name = 'Название цвета', default='Бежевый', null=True)
	color_code = models.CharField(max_length=50, verbose_name = 'Цвет в #HEX', default='#E5E1DF', null=True)

	class Meta:
		ordering = ['color_name']
		indexes = [
			models.Index(fields=['color_name']),
		]
		verbose_name = 'Цвет HEX или RGBA'
		verbose_name_plural = 'Цвета HEX или RGBA'
	def __str__(self):
		return self.color_name


class Car(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	status = models.ForeignKey(Status,
		related_name='statuses',
		on_delete=models.CASCADE, verbose_name = 'Новая/Уже нет')
	color = models.ForeignKey(Color,
		related_name='colors',
		on_delete=models.CASCADE, verbose_name = 'Цвет', null=True)

	name = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Название модели')
	price = models.IntegerField(max_length=25, null=True, blank=True, verbose_name = 'Цена')
	price_old = models.IntegerField(max_length=25, null=True, blank=True, verbose_name = 'Цена БЕЗ скидки')
	year = models.CharField(max_length=4, null=True, blank=True, verbose_name = 'Год выпуска')
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





###############

# ABOUT FORMS #

###############



class CallMe(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка: перезвоните мне'
		verbose_name_plural = 'Заявки: перезвоните мне'
	def __str__(self):
		return self.first_name


class CallMeItem(models.Model):
	callme_order = models.ForeignKey(CallMe,related_name='items', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
	    return str(self.id)




class WantThisCar(models.Model):
	id = models.AutoField(primary_key=True)
	car_name = models.CharField(max_length=30, verbose_name = 'Марка машины')
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Хочу такую же'
		verbose_name_plural = 'Запросы: хочу такую же!'

	def __str__(self):
		return self.first_name

class CallMeItem(models.Model):
	order = models.ForeignKey(CallMe,related_name='items', on_delete=models.CASCADE)
	car = models.ForeignKey(Car, related_name='order_items', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
	    return str(self.id)




class CarSurveyFull(models.Model):
	id = models.AutoField(primary_key=True)
	car_characteristics =  models.CharField(max_length=300, verbose_name = 'Марка, модель, мотор', null=True, blank=True)
	country = models.CharField(max_length=300, verbose_name = 'Из какой страны Вас интересует автомобиль?', null=True, blank=True)
	when =  models.CharField(max_length=300, verbose_name = 'Когда планируете покупать? ', null=True, blank=True)
	payment_type =  models.CharField(max_length=300, verbose_name = 'Форма оплаты за автомобиль?', null=True, blank=True)
	max_price =  models.CharField(max_length=300, verbose_name = 'Максимальный бюджет для покупки?', null=True, blank=True)
	trade_in =  models.CharField(max_length=300, verbose_name = 'Планируете трейд ин? Какой авто? Пробег?', null=True, blank=True)
	complectation =  models.CharField(max_length=600, verbose_name = 'Комплектация?', null=True, blank=True)
	colors =  models.CharField(max_length=300, verbose_name = 'Желаемые цвета кузова и салона', null=True, blank=True)
	need_casco = models.BooleanField(verbose_name = 'Планируете ли делать Каско?', default=True)
	real_price =  models.CharField(max_length=300, verbose_name = 'Какова стоимость реального предложения автомобиля, которое Вам удалось найти?', null=True, blank=True)

	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заказ машины: подробный опросник'
		verbose_name_plural = 'Заказ машины: подробный опросник'

	def __str__(self):
		return self.first_name



class GuaranteeCount(models.Model):
	id = models.AutoField(primary_key=True)
	who_sold = models.BooleanField(verbose_name = 'Авто куплено через R.E.D. Group?', default=True)
	have_goverment_number = models.BooleanField(verbose_name = 'Есть ли Гос. номер?', default=True)
	goverment_number = models.CharField(max_length=30, verbose_name = 'Если да, укажите:', null=True, blank=True)
	is_gai_record = models.BooleanField(verbose_name = 'Поставлена ли машина на учёт?', default=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка на рассчет гарантии'
		verbose_name_plural = 'Заявки на рассчет гарантии'

	def __str__(self):
		return self.first_name



class NeedDiagnostic(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	urgency = models.BooleanField(verbose_name = 'Срочно?', default=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка на диагностику'
		verbose_name_plural = 'Заявки на диагностику'

	def __str__(self):
		return self.first_name



class NeedServece(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	urgency = models.BooleanField(verbose_name = 'Срочно?', default=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка на сервисное обслуживание'
		verbose_name_plural = 'Заявки на сервисное обслуживание'

	def __str__(self):
		return self.first_name



class ShesterenkyNeed(models.Model):
	id = models.AutoField(primary_key=True)
	year = models.CharField(max_length=30, verbose_name = 'Год выпуска', null=True, blank=True)
	vin = models.CharField(max_length=30, verbose_name = 'VIN-номер', null=True, blank=True)
	its_name = models.CharField(max_length=100, verbose_name = 'Название детали', null=True, blank=True)
	img = models.ImageField(upload_to='spares/', null=True, blank=True, verbose_name = 'Фото детали')

	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка на запчасть'
		verbose_name_plural = 'Заявки на запчасти'

	def __str__(self):
		return self.first_name



class CascoCount(models.Model):
	id = models.AutoField(primary_key=True)
	budget =  models.CharField(max_length=30, verbose_name = 'Какой бюджет?', default=True)
	type = models.CharField(max_length=30, verbose_name = 'Дизель / электрокар?', null=True, blank=True)

	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка на рассчет КАСКО'
		verbose_name_plural = 'Заявки на рассчет КАСКО'

	def __str__(self):
		return self.first_name



class LegalHelp(models.Model):
	id = models.AutoField(primary_key=True)
	where_auto = models.CharField(max_length=300, verbose_name = '  Где сейчас находится авто? В РФ/в др.стране/на таможне?', null=True, blank=True)
	documents = models.CharField(max_length=300, verbose_name = ' Какие документы у вас есть сейчас?', null=True, blank=True)

	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Запрос юридической поддержки'
		verbose_name_plural = 'Запросы юридической поддержки'

	def __str__(self):
		return self.first_name