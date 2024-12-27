from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Subject',
    'Test Body',
    settings.EMAIL_HOST_USER,
    ['sales@rgspace.pro'],
)