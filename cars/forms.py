from django import forms
from .models import CallMe, CarSurvey_Full


class CallMeForm(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']

class CarSurvey_Full(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']	