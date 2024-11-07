from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import *

import logging
import time
logger = logging.getLogger(__name__)



@shared_task(max_retries=3)
def send_email_callme(first_name, phone):
	logger.info(f"Preparing to send email for: {first_name}, {phone}")
	
	subject = f'Заявка на звонок | {first_name}, {phone}'
	body = (
	f'Привет, продаван!\n\nПоступила новая заявка на обратный звонок. Данные клиента:\n\nИмя: {first_name}\nТелефон {phone}'
	)
	recipient_list = ['to.the.neizvestnost@yandex.ru']

	try:
		send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
		logger.info(f"Email sent from {settings.EMAIL_HOST_USER} to {recipient_list}")
	except Exception as e:
		logger.error(f"Error sending email: {e}")
		raise self.retry(exc=e, countdown=5)