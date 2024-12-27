import os
import mimetypes
from celery import shared_task
from django.core.mail import send_mail, EmailMessage
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
def send_email_want_this_car_form(name, phone, car_name):
    subject = f"{name} хочет {car_name} ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nМодель: {car_name}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_car_survey_full_form(name, phone, car_characteristics, country, when, payment_type, max_price, trade_in, complectation, colors, need_casco, real_price):
    subject = f"Заявка с подробными хотелками | {name} ☎ {phone}"
    body = f"Имя: {name}\nТелефон: {phone}\n\nМарка, модель, мотор: {car_characteristics}\nИз какой страны вас интересует автомобиль: {country}\nКогда планируете покупку: {when}\nФорма оплаты за автомобиль: {payment_type}\nМаксимальный бюджет покупки: {max_price}\nПланируете трейд ин? Какой авто? Пробег? {trade_in}\nЖелаемая комплектация: {complectation}\nЖелаемые цвета кузова и салона: {colors}\nПланируете оформлять КАСКО? {need_casco}\nКакова стоимость реального предложения автомобиля, которое Вам удалось найти? {real_price}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_guarantee_count_form(who_sold, have_goverment_number, goverment_number, is_gai_record, name, phone):
    subject = f"{name} хочет оформить гарантию! ☎ {phone}"
    body = f"Имя: {name}\nТелефон: {phone}\n\nАвто куплено через R.E.D. Group? {who_sold}\nЕсть ли Гос. номер? {have_goverment_number}\nЕсли да, укажите: {goverment_number}\n Есть регистрация в ГАИ? {is_gai_record}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")


@shared_task
def send_email_need_diagnostic_form(name, phone, urgency):
    subject = f"{name} хочет на диагностику! ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone} \n\nСрочно? {urgency}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_need_service_form(name, phone, urgency):
    subject = f"{name} хочет на сервисное обслуживание ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone} \n\nСрочно? {urgency}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_shesterenky_need_form(year, vin, its_name, img_file, name, phone):

    subject = f"{name} хочет запчасть {its_name} ☎ {phone}"

    body = f"Имя: {name}\n\nТелефон: {phone}\n\nГод выпуска: {year}\n\nVIN-номер: {vin}\n\nНазвание: {its_name}\n\nИзображение прикреплено к письму файлом"

    email = EmailMessage(subject, body, settings.EMAIL_HOST_USER, ['service@rgspace.pro'])

    if img_file:
        try:
            with open(img_file, 'rb') as the_img_file:
                mime_type, _ = mimetypes.guess_type(the_img_file.name)
                if mime_type is None:
                    mime_type = 'application/octet-stream'
                email.attach(os.path.basename(the_img_file.name), the_img_file.read(), mime_type)
        except Exception as e:
            logger.error(f"Failed to attach image: {e}")
    try:
        email.send()
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")


    # try:
    #     send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
    #     logger.info(f"Email sent from {name}")
    # except Exception as e:
    #     logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_casco_count_form(budget, type, name, phone):
    subject = f"{name} хочет КАСКО ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nБюджет: {budget}\n\nТип: {type}"
    recipient_list = ['service@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")



@shared_task
def send_email_legal_help_form(where_auto, documents, name, phone):
    subject = f"{name} нужна юр.поддержка ☎ {phone}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nГде сейчас находится автомобиль: {where_auto}\n\nКакие есть документы: {documents}"
    recipient_list = ['sales@rgspace.pro']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
