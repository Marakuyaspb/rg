from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Category, Status, Car




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id_cat', 'category']
	list_filter = ['category']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ['id_st', 'status']
	list_filter = ['status']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ['id', 'category', 'status', 'name', 'price', 'price_old', 'available']
	list_filter = ['name']