from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id_cat', 'category']
	list_filter = ['category']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = ['color_id', 'color_name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ['id_st', 'status']
	list_filter = ['status']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ['id', 'category', 'status', 'name', 'price', 'price_old', 'available']
	list_filter = ['name']



###############

# ABOUT FORMS #

###############


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['first_name', 'phone', 'created']

@admin.register(WantThisCar)
class WantThisCarAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['car_name', 'first_name', 'phone', 'created']

@admin.register(CarSurveyFull)
class CarSurveyFullAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = [
		'car_characteristics',
		'country', 
		'when',
		'payment_type',
		'max_price',
		'trade_in',
		'complectation',
		'colors',
		'need_casco',
		'real_price',
		'first_name',
		'phone',
		'created'
	]

@admin.register(GuaranteeCount)
class GuaranteeCountAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = [
		'who_sold',
		'have_goverment_number',
		'goverment_number',
		'is_gai_record',
		'first_name',
		'phone', 
		'created'
	]

@admin.register(NeedDiagnostic)
class NeedDiagnosticAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['urgency', 'first_name', 'phone', 'created']

@admin.register(NeedServece)
class NeedServeceAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['urgency','first_name', 'phone', 'created']

@admin.register(ShesterenkyNeed)
class ShesterenkyNeedAdmin(admin.ModelAdmin):
	list_display = ['year', 'vin', 'its_name', 'get_html_img_preview','first_name', 'phone', 'created']
	readonly_fields = [
		'year',
		'vin',
		'its_name',
		'img',
		'get_html_img_preview',
		'first_name',
		'phone',
		'created'
	]

	# show preview
	def get_html_img_preview(self, obj):
		if obj.img:
			return mark_safe(f'<img src="{obj.img.url}" width=200>')
		return "No Image"
	get_html_img_preview.short_description = 'Превью'


@admin.register(CascoCount)
class CascoCountAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['budget', 'type', 'first_name', 'phone', 'created']

@admin.register(LegalHelp)
class LegalHelpAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	readonly_fields = ['where_auto', 'documents', 'first_name', 'phone', 'created']