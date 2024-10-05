from io import BytesIO
from django.conf import settings
from celery import shared_task
import weasyprint

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Order


@shared_task
def callme_created(order_id):
  order = Order.objects.get(id=order_id)
  subject = f'Новая заявка № {order.id}'
  message = (
    f'Привет, продаван!\n\n'
    f'Поступила новая заявка на обратный звонок. Данные клиента:'
    f'Имя: {order.first_name}'
    f'Телефон {order.phone}'
    )

  email = EmailMessage(
    subject,
    message,
    'settings.EMAIL_HOST_USER',
    [settings.EMAIL_HOST_USER]
  )

  email.send()