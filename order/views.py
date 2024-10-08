import os
import logging

from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from .tasks import *
from .models import *
from .forms import *


logging.basicConfig(filename='mail_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

#ПРОСТО ЗАКАЗ
def callme_order_create(request):
	callme_order = CallMe(request)
	if request.method == 'POST':
		form = CallMeForm(request.POST)
		if form.is_valid():
			callme_order = form.save()
			CallMeItem.objects.create(callme_order=callme_order, first_name='first_name', phone='phone')

		# SEND EmAIL TO MANAGER
			context = {
			  'callme_order': callme_order,
			}
			try:
				send_mail('Новый заказ',
					'Здавствуйте!', 
					settings.EMAIL_HOST_USER,
					['aa@madfox.io'],
					fail_silently=True,
					html_message=loader.get_template('orders/order/mail_CallMe.html').render(context)
				)
				logging.info(f"Mail to manager send successfully")
			except Exception as e:
				logging.error(f"Error sending mail to: {str(e)}")
			return render(request, 'orders/order/created.html', {'callme_order': callme_order})
	else:
		callme_form = CallMeForm()
	return render(request, 'orders/order/create.html', {'callme_form': callme_form})



@staff_member_required
def admin_carSurveyFull_detail(request, id):
	carsurveyfull = get_object_or_404(CarSurveyFull, id=id)
	return render(request, 'orders/order/detail.html', {'carsurveyfull': carsurveyfull})