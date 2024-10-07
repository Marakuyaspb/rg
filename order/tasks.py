from io import BytesIO
from django.conf import settings
from celery import shared_task
import weasyprint

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *


@shared_task
def callme_created(order_id):
  callme = CallMe.objects.get(id=id)
  subject = f'Новая заявка № {callme.id}'
  message = (
    f'Привет, продаван!\n\n'
    f'Поступила новая заявка на обратный звонок. Данные клиента:'
    f'Имя: {callme.first_name}'
    f'Телефон {callme.phone}'
    )

  email = EmailMessage(
    subject,
    message,
    'settings.EMAIL_HOST_USER',
    [settings.EMAIL_HOST_USER]
  )
  email.send()



@shared_task
def want_this_car_created(order_id):
  want_this_car = WantThisCar.objects.get(id=id)
  subject = f'Новая заявка № {want_this_car.id}'
  message = (
    f'Привет, продаван!\n\n'
    f'Поступила новая заявка авто. Данные клиента:'
    f'Имя: {want_this_car.first_name}'
    f'Телефон {want_this_car.phone}'
    f'Детали: {want_this_car.car_name}'
    )

  email = EmailMessage(
    subject,
    message,
    'settings.EMAIL_HOST_USER',
    [settings.EMAIL_HOST_USER]
  )
  email.send()