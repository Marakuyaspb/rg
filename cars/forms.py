from django import forms
from .models import CallMe


class CallMeForm(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone', 'email']