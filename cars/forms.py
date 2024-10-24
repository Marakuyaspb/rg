from django import forms
from .models import *


# class FilterForm(forms.Form):
# 	color_id = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False)


class CallMeForm(forms.Form):
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']


class WantThisCarForm(forms.Form):
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)
	car_name = forms.CharField(widget=forms.HiddenInput())


class CarSurveyFullForm(forms.Form):
	CHOICES = [
		('да', 'да'),
		('нет', 'нет'),
	]

	car_characteristics = forms.CharField(label="Марка, модель, мотор")
	country = forms.CharField(label="Из какой страны вас интересует автомобиль?")
	when =  forms.CharField(label="Когда планируете покупать?")
	payment_type =  forms.CharField(label="Форма оплаты за автомобиль?")
	max_price =  forms.CharField(label="Максимальный бюджет покупки?")
	trade_in =  forms.CharField(label="Планируете трейд ин? Какой авто? Пробег?",max_length=300)
	complectation =  forms.CharField(label="Какую вы хотите комплектацию?")
	colors = forms.CharField(label="Желаемые цвета кузова и салона")
	need_casco = forms.ChoiceField(label="Планируете ли делать КАСКО?", choices = CHOICES)
	real_price =  forms.CharField(label="Какова стоимость реального предложения автомобиля, которое Вам удалось найти?")
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон",required=True)


class GuaranteeCountForm(forms.Form):
	CHOICES = [
		('да', 'да'),
		('нет', 'нет'),
	]

	who_sold = forms.ChoiceField(label='Авто куплено через R.E.D. Group?', choices = CHOICES)
	have_goverment_number = forms.ChoiceField(label="Есть ли Гос. номер?", choices = CHOICES)
	goverment_number = forms.CharField(label="Если да, укажите")
	is_gai_record = forms.ChoiceField(label="Поставлена ли машина на учёт?", choices = CHOICES)
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)


class NeedDiagnosticForm(forms.Form):
	CHOICES = [
		('да', 'да'),
		('нет', 'нет'),
	]

	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)
	urgency = forms.ChoiceField(label="Срочно?", choices = CHOICES)


class NeedServeceForm(forms.Form):
	CHOICES = [
		('да', 'да'),
		('нет', 'нет'),
	]
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)
	urgency = forms.ChoiceField(label="Срочно?", choices = CHOICES)


class ShesterenkyNeedForm(forms.Form):
	year = forms.CharField(label="Телефон", required=True)
	vin = forms.CharField(label="Телефон", required=True)
	its_name = forms.CharField(label="Телефон",max_length=100)
	img = forms.ImageField(label="Телефон")
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)


class CascoCountForm(forms.Form):
	budget =  forms.CharField(label="Телефон", required=True, )
	type = forms.CharField(label="Телефон", required=True)
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)


class LegalHelpForm(forms.Form):
	where_auto = forms.CharField(label="Телефон", required=True)
	documents = forms.CharField(label="Телефон", required=True)
	first_name = forms.CharField(label="Имя", required=True)
	phone = forms.CharField(label="Телефон", required=True)