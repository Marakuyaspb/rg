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