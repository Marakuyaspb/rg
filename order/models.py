from django.db import models
from cars.models import Car


class CallMe(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=30, verbose_name='Телефон')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'Заявка: перезвоните мне'
		verbose_name_plural = 'Заявки: перезвоните мне'

	def __str__(self):
		return self.first_name



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