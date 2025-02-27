import os
import logging
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template import loader

from .forms import *
from .models import *
from .tasks import * 


logging.basicConfig(filename='mail_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


# JUST CALL ME / phone + name /
def handle_callme_form(request):
    if request.method == 'POST':
        callme_form = CallMeForm(request.POST)
        if callme_form.is_valid():
            callme = callme_form.save()

            send_email_callme_form.delay(
                callme.first_name, 
                callme.phone
            )
            return callme_form
    else:
        callme_form = CallMeForm()
    return callme_form


# WANT THIS CAR
def handle_want_this_car_form(request):
    if request.method == 'POST':
        car_name = request.POST.get('car_name')
        want_this_car_form = WantThisCarForm(request.POST)

        if want_this_car_form.is_valid(): 
            want_this_car = want_this_car_form.save(commit=False)
            want_this_car.car_name = car_name
            want_this_car.save()
            
            send_email_want_this_car_form.delay(
                want_this_car.first_name, 
                want_this_car.phone,
                want_this_car.car_name
            )
            return want_this_car_form

        else:
            print(want_this_car_form.errors)
            want_this_car_form = WantThisCarForm()
    return want_this_car_form


# CAR SURVEY FULL
def handle_car_survey_full_form(request):
    if request.method == 'POST':
        car_survey_full_form = CarSurveyFullForm(request.POST)
        if car_survey_full_form.is_valid():
            car_survey_full = car_survey_full_form.save()
            
            send_email_car_survey_full_form.delay(
                car_survey_full.car_characteristics, 
                car_survey_full.country,
                car_survey_full.when,
                car_survey_full.payment_type,
                car_survey_full.max_price,
                car_survey_full.trade_in,
                car_survey_full.complectation,
                car_survey_full.colors,
                car_survey_full.need_casco,
                car_survey_full.real_price,
                car_survey_full.first_name,
                car_survey_full.phone
            )
            return car_survey_full_form
    else:
        car_survey_full_form = CarSurveyFullForm()
    return car_survey_full_form


# GUARANTEE COUNT
def handle_guarantee_count_form(request):
    if request.method == 'POST':
        guarantee_count_form = GuaranteeCountForm(request.POST)
        if guarantee_count_form.is_valid():
            guarantee_count = guarantee_count_form.save()
            
            send_email_guarantee_count_form.delay(
                guarantee_count.who_sold,
                guarantee_count.have_goverment_number,
                guarantee_count.goverment_number,
                guarantee_count.is_gai_record,
                guarantee_count.first_name,
                guarantee_count.phone
            )
            return guarantee_count_form 
    else:
        guarantee_count_form = GuaranteeCountForm()
    return guarantee_count_form


# NEED DIAGNOSTIC
def handle_need_diagnostic_form(request):
    if request.method == 'POST':
        need_diagnostic_form = NeedDiagnosticForm(request.POST)
        if need_diagnostic_form.is_valid():
            need_diagnostic = need_diagnostic_form.save()
            
            send_email_need_diagnostic_form.delay(
                need_diagnostic.first_name,
                need_diagnostic.phone,
                need_diagnostic.urgency
            )
            return need_diagnostic_form 
    else:
        need_diagnostic_form = NeedDiagnosticForm()
    return need_diagnostic_form


# NEED SERVICE
def handle_need_service_form(request):
    if request.method == 'POST':
        need_service_form = NeedServeceForm(request.POST)
        if need_service_form.is_valid():
            need_service = need_service_form.save()
            send_email_need_service_form.delay(
                need_service.first_name,
                need_service.phone,
                need_service.urgency
            )
            print(os.getenv('TW_MAIL'))
            return need_service_form 
    else:
        need_service_form = NeedServeceForm()
    return need_service_form


# SHESTERENKY COUNT
def handle_shesterenky_need_form(request):
    if request.method == 'POST':
        shesterenky_need_form = ShesterenkyNeedForm(request.POST, request.FILES)
        if shesterenky_need_form.is_valid():
            shesterenky_need = shesterenky_need_form.save()
            img_file = None

            if shesterenky_need.img:
                img_file = shesterenky_need.img.path

            send_email_shesterenky_need_form.delay(
                shesterenky_need.year,
                shesterenky_need.vin,
                shesterenky_need.its_name,
                img_file,
                shesterenky_need.first_name,
                shesterenky_need.phone,
            )
            return shesterenky_need_form 
    else:
        shesterenky_need_form = ShesterenkyNeedForm()
    return shesterenky_need_form


# CASCO COUNT
def handle_casco_count_form(request):
    if request.method == 'POST':
        casco_count_form = CascoCountForm(request.POST)
        if casco_count_form.is_valid():
            casco_count = casco_count_form.save()
            send_email_casco_count_form.delay(
                casco_count.budget,
                casco_count.type,
                casco_count.first_name,
                casco_count.phone
            )
            return casco_count_form 
    else:
        casco_count_form = CascoCountForm()
    return casco_count_form


# LEGAL HELP
def handle_legal_help_form(request):
    if request.method == 'POST':
        legal_help_form = LegalHelpForm(request.POST)
        if legal_help_form.is_valid():
            legal_help = legal_help_form.save()
            send_email_legal_help_form.delay(
                legal_help_form.cleaned_data['where_auto'],
                legal_help_form.cleaned_data['documents'],
                legal_help_form.cleaned_data['first_name'],
                legal_help_form.cleaned_data['phone']
            )
            return legal_help_form 
    else:
        legal_help_form = LegalHelpForm()
    return legal_help_form