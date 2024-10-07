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



@staff_member_required
def admin_carSurveyFull_detail(request, id):
	carsurveyfull = get_object_or_404(CarSurveyFull, id=id)
	return render(request, 'orders/order/detail.html', {'carsurveyfull': carsurveyfull})