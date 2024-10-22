from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
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

@admin.register(WantThisCar)
class WantThisCarAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(CarSurveyFull)
class CarSurveyFullAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(GuaranteeCount)
class GuaranteeCountAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(NeedDiagnostic)
class NeedDiagnosticAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(NeedServece)
class NeedServeceAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']
	
@admin.register(ShesterenkyNeed)
class ShesterenkyNeedAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(CascoCount)
class CascoCountAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']

@admin.register(LegalHelp)
class LegalHelpAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'created']