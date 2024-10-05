from django import forms
from .models import CallMe, CarSurvey_Full


class CallMeForm(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']
		

class CarSurvey_Full(forms.ModelForm):
	class Meta:
		model = CarSurvey_Full
		fields = ['first_name', 'phone','car_characteristics' ,'country', 'when', 'payment_type', 'max_price','', 'trade_in','complectation','colors','need_casco','real_price']