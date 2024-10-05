from django.db import models
from cars.models import Car


class Order(models.Model):
	first_name = models.CharField(max_length=60, verbose_name = 'Ваше имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-created']
		indexes = [
		models.Index(fields=['-created']),
		]
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return f'Order {self.id}'

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	car = models.ForeignKey(Car, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return str(self.id)
		
	def get_cost(self):
		return self.price * self.quantity