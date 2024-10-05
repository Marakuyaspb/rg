from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Category, Status, Car
from .forms import CallMe, CarSurveyFull, GuaranteeCount, NeedDiagnostic, NeedServece, ShesterenkyNeed, CascoCount, LegalHelp




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



# ALL FORMS HERE

@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'created']
	list_filter = ['created']

@admin.register(CarSurveyFull)
class CarSurveyFullAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'phone', 'max_price', 'payment_type', 'created']
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