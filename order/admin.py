from django.contrib import admin
from pathlib import Path
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *



@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'created']
	list_filter = ['created']

@admin.register(WantThisCar)
class WantThisCarAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'created']
	list_filter = ['created']


@admin.register(GuaranteeCount)
class GuaranteeCountAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'who_sold', 'have_goverment_number', 'goverment_number', 'is_gai_record', 'created']
	list_filter = ['created']

@admin.register(NeedDiagnostic)
class NeedDiagnosticAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'urgency', 'created']
	list_filter = ['created']

@admin.register(NeedServece)
class NeedServeceAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'urgency', 'created']
	list_filter = ['created']

@admin.register(ShesterenkyNeed)
class ShesterenkyNeedAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'its_name', 'created']
	list_filter = ['created']

@admin.register(CascoCount)
class CascoCountAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'budget', 'created']
	list_filter = ['created']

@admin.register(LegalHelp)
class LegalHelpAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'where_auto', 'documents', 'created']
	list_filter = ['created']



# GIANT form
def CarSurveyFull_detail(obj):
	url = reverse('order:admin_CarSurveyFull_detail', args=[obj.id])
	return mark_safe(
		f'<a href="{url}">Подробно</a>'
	)
	
@admin.register(CarSurveyFull)
class CarSurveyFullAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'max_price', 'payment_type', 'created', CarSurveyFull_detail]
	list_filter = ['created']


