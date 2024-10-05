from django import forms
from .models import *


class CallMeForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']


class WantThisCarForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)
	car_id = forms.CharField(max_length=30)


class CarSurveyFullForm(forms.Form):
	car_characteristics =  forms.CharField(max_length=300)
	country = forms.CharField(max_length=300)
	when =  forms.CharField(max_length=300)
	payment_type =  forms.CharField(max_length=300)
	max_price =  forms.CharField(max_length=300)
	trade_in =  forms.CharField(max_length=300)
	complectation =  forms.CharField(max_length=600)
	colors =  forms.CharField(max_length=300)
	need_casco = forms.BooleanField()
	real_price =  forms.CharField(max_length=300)
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)


class GuaranteeCountForm(forms.Form):
	who_sold = forms.BooleanField()
	have_goverment_number = forms.BooleanField()
	goverment_number = forms.CharField(max_length=30)
	is_gai_record = forms.BooleanField()
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)


class NeedDiagnosticForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)
	urgency = forms.BooleanField()


class NeedServeceForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)
	urgency = forms.BooleanField()


class ShesterenkyNeedForm(forms.Form):
	year = forms.CharField(max_length=30)
	vin = forms.CharField(max_length=30)
	its_name = forms.CharField(max_length=100)
	img = forms.ImageField()
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)


class CascoCountForm(forms.Form):
	budget =  forms.CharField(max_length=30, )
	type = forms.CharField(max_length=30)
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)


class LegalHelpForm(forms.Form):
	where_auto = forms.CharField(max_length=300)
	documents = forms.CharField(max_length=300)
	first_name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=30)