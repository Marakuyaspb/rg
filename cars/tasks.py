from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_email_callme_form(name, phone):
    subject = f"Заявка на звонок | {name} ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_want_this_car_form(name, phone):
    subject = f"{name} хочет {car_name} ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nМодель: {car_name}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_car_survey_full_form(name, phone):
    subject = f"Заявка с подробными хотелками | {name} ☎ {phone}"
    body = f"Имя: {name}\nТелефон: {phone}\n\nМарка, модель, мотор: {car_characteristics}\nИз какой страны вас интересует автомобиль: {country}\nКогда планируете покупку: {when}\nФорма оплаты за автомобиль: {payment_type}\nМаксимальный бюджет покупки: {max_price}\nПланируете трейд ин? Какой авто? Пробег? {trade_in}\nЖелаемая комплектация: {complectation}\nЖелаемые цвета кузова и салона: {colors}\nПланируете оформлять КАСКО? {need_casco}\nКакова стоимость реального предложения автомобиля, которое Вам удалось найти? {real_price}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_guarantee_count_form(name, phone):
    subject = f"{name} хочет оформить гарантию! ☎ {phone}"
    body = f"Имя: {name}\nТелефон: {phone}\n\nАвто куплено через R.E.D. Group? {who_sold}\nЕсть ли Гос. номер? {have_goverment_number}\nЕсли да, укажите: {goverment_number}\n Есть регистрация в ГАИ? {is_gai_record}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")


@shared_task
def send_email_need_diagnostic_form(name, phone):
    subject = f"{name} хочет на диагностику! ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone} \n\nСрочно? {urgency}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_need_service_form(name, phone):
    subject = f"{name} хочет на сервисное обслуживание ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone} \n\nСрочно? {urgency}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_shesterenky_need_form(name, phone):
    subject = f"{name} хочет запчасть {its_name} ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nГод выпуска: {year}\n\nVIN-номер: {vin}\n\nНазвание: {its_name}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_casco_count_form(name, phone):
    subject = f"{name} хочет КАСКО ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nБюджет: {budget}\n\nТип: {type}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_legal_help_form(name, phone):
    subject = f"{name} нужна юр.поддержка ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nГде сейчас находится автомобиль: {where_auto}\n\nКакие есть документы: {documents}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
