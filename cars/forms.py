from django import forms
from .models import *



class CallMeForm(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон',
		}


class WantThisCarForm(forms.ModelForm):
	class Meta:
		model = WantThisCar
		fields = ['first_name', 'phone', 'car_name']
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон',
		}
		# car_name = forms.CharField(widget=forms.HiddenInput())


class CarSurveyFullForm(forms.ModelForm):
	CHOICES = [
		(True, 'Да'),
		(False, 'Нет'),
	]
	need_casco = forms.ChoiceField(
		choices=CHOICES,
		widget=forms.RadioSelect, 
		required=False 
	)

	class Meta:
		model = CarSurveyFull
		fields = [
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
		'phone'
		]
		labels = {
		'car_characteristics': 'Марка, модель, мотор',
		'country': 'Из какой страны вас интересует автомобиль?',
		'when': 'Когда планируете покупку?',
		'payment_type': 'Форма оплаты за автомобиль?',
		'max_price': 'Максимальный бюджет покупки?',
		'trade_in': 'Планируете трейд ин? Какой авто? Пробег?',
		'complectation': 'Какую вы хотите комплектацию?',
		'colors': 'Желаемые цвета кузова и салона',
		'need_casco': 'Планируете оформлять КАСКО?',
		'real_price': 'Какова стоимость реального предложения автомобиля, которое Вам удалось найти?',
		'first_name': 'Имя',
		'phone': 'Телефон'
		}



class GuaranteeCountForm(forms.ModelForm):
	CHOICES = [
		(True, 'Да'),
		(False, 'Нет'),
	]
	is_gai_record = forms.ChoiceField(
		choices=CHOICES,
		widget=forms.RadioSelect, 
		required=False 
	)
	class Meta:
		model = GuaranteeCount
		fields = [
		'who_sold',
		'have_goverment_number',
		'goverment_number',
		'is_gai_record',
		'first_name',
		'phone'
		]
		labels = {
		'who_sold': 'Авто куплено через R.E.D. Group?',
		'have_goverment_number': 'Есть ли Гос. номер?',
		'goverment_number': 'Планируете оформлять КАСКО?',
		'is_gai_record': 'Если да, укажите',
		'first_name': 'Имя',
		'phone': 'Телефон'
		}



class NeedDiagnosticForm(forms.ModelForm):
	CHOICES = [
		(True, 'Да'),
		(False, 'Нет'),
	]
	urgency = forms.ChoiceField(
		choices=CHOICES,
		widget=forms.RadioSelect, 
		required=False 
	)
	class Meta:
		model = NeedDiagnostic
		fields = [
		'first_name',
		'phone',
		'urgency'
		]
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон',
		'urgency': 'Срочно?',
		}


class NeedServeceForm(forms.ModelForm):
	CHOICES = [
		(True, 'Да'),
		(False, 'Нет'),
	]
	urgency = forms.ChoiceField(
		choices=CHOICES,
		widget=forms.RadioSelect, 
		required=False 
	)
	class Meta:
		model = NeedServece
		fields = [
		'first_name',
		'phone',
		'urgency'
		]
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон',
		'urgency': 'Срочно?',
		}


class ShesterenkyNeedForm(forms.ModelForm):
	class Meta:
		model = ShesterenkyNeed
		fields = [
		'year',
		'vin',
		'its_name',
		'img',
		'first_name',
		'phone'

		]
		labels = {
		'year': 'Год выпуска',
		'vin': 'VIN-номер',
		'its_name': 'Название',
		'img': 'Фото (если есть)',
		'first_name': 'Имя',
		'phone': 'Телефон'
		}


class CascoCountForm(forms.ModelForm):
	class Meta:
		model = CascoCount
		fields = [
		'budget',
		'type',
		'first_name',
		'phone'
		]
		labels = {
		'budget': 'Бюджет',
		'type': 'Тип',
		'first_name': 'Имя',
		'phone': 'Телефон'
		}


class LegalHelpForm(forms.ModelForm):
	class Meta:
		model = LegalHelp
		fields = [
		'where_auto',
		'documents',
		'first_name',
		'phone'
		]
		labels = {
		'where_auto': 'Где сейчас находится машина?',
		'documents': 'Какие у вас есть документы?',
		'first_name': 'Имя',
		'phone': 'Телефон'
		}