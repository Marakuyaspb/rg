from order.forms import *
from order.models import *
from .models import *
from order.tasks import * 




# JUST CALL ME / phone + name /
def handle_callme_form(request):
    if request.method == 'POST':
        callme_form = CallMeForm(request.POST)
        if callme_form.is_valid():
            callme = CallMe(
                first_name=callme_form.cleaned_data['first_name'],
                phone=callme_form.cleaned_data['phone']
            )
            callme.save()
            callme_created.delay(callme.first_name)
        return callme_form 
    else:
        callme_form = CallMeForm()

    return callme_form




# WANT THIS CAR
def handle_want_this_car_form(request):
    if request.method == 'POST':
        want_this_car_form = WantThisCarForm(request.POST)
        if want_this_car_form.is_valid():
            want_this_car = WantThisCar(
                first_name=want_this_car_form.cleaned_data['first_name'],
                phone=want_this_car_form.cleaned_data['phone'],
                car_name=want_this_car_form.cleaned_data['car_name']
            )
            want_this_car.save()
            want_this_car_created.delay(want_this_car.first_name)
        return want_this_car_form 
    else:
        want_this_car_form = WantThisCarForm()

    return want_this_car_form




# CAR SURVEY FULL
def handle_car_survey_full_form(request):
    if request.method == 'POST':
        car_survey_full_form = CarSurveyFullForm(request.POST)
        if car_survey_full_form.is_valid():
            car_survey_full = CarSurveyFull(    
                car_characteristics=car_survey_full_form.cleaned_data['car_characteristics'],
                country=car_survey_full_form.cleaned_data['country'],
                when=car_survey_full_form.cleaned_data['when'],
                payment_type=car_survey_full_form.cleaned_data['payment_type'],
                max_price=car_survey_full_form.cleaned_data['max_price'],
                trade_in=car_survey_full_form.cleaned_data['trade_in'],
                complectation=car_survey_full_form.cleaned_data['complectation'],
                colors=car_survey_full_form.cleaned_data['colors'],
                need_casco=car_survey_full_form.cleaned_data['need_casco'],
                real_price=car_survey_full_form.cleaned_data['real_price'],
                first_name=car_survey_full_form.cleaned_data['first_name'],
                phone=car_survey_full_form.cleaned_data['phone'],
            )
            car_survey_full.save()
            car_survey_full_created.delay(car_survey_full.first_name)
        return car_survey_full_form 
    else:
        car_survey_full_form = CarSurveyFullForm()

    return survey_full_form




# GUARANTEE COUNT
def handle_guarantee_count_form(request):
    if request.method == 'POST':
        guarantee_count_form = GuaranteeCountForm(request.POST)
        if guarantee_count_form.is_valid():
            guarantee_count = WantThisCar(
                who_sold=guarantee_count_form.cleaned_data['who_sold'],
                have_goverment_number=guarantee_count_form.cleaned_data['have_goverment_number'],
                goverment_number=guarantee_count_form.cleaned_data['goverment_number'],
                is_gai_record=guarantee_count_form.cleaned_data['is_gai_record'],
                first_name=guarantee_count_form.cleaned_data['first_name'],
                phone=guarantee_count_form.cleaned_data['phone']
            )
            guarantee_count.save()
            guarantee_count_created.delay(guarantee_count.first_name)
        return guarantee_count_form 
    else:
        guarantee_count_form = GuaranteeCountForm()

    return guarantee_count_form




# NEED DIAGNOSTIC
def handle_need_diagnostic_form(request):
    if request.method == 'POST':
        need_diagnostic_form = NeedDiagnosticForm(request.POST)
        if need_diagnostic_form.is_valid():
            need_diagnostic = WantThisCar(
                first_name=need_diagnostic_form.cleaned_data['first_name'],
                phone=need_diagnostic_form.cleaned_data['phone'],
                urgency=need_diagnostic_form.cleaned_data['urgency']
            )
            need_diagnostic.save()
            need_diagnostic_created.delay(need_diagnostic.first_name)
        return need_diagnostic_form 
    else:
        need_diagnostic_form = NeedDiagnosticForm()

    return need_diagnostic_form




# NEED SERVICE
def handle_need_service_form(request):
    if request.method == 'POST':
        need_service_form = NeedServeceForm(request.POST)
        if need_service_form.is_valid():
            need_service = WantThisCar(
                first_name=need_service_form.cleaned_data['first_name'],
                phone=need_service_form.cleaned_data['phone'],
                urgency=need_service_form.cleaned_data['urgency']
            )
            need_service.save()
            need_service_created.delay(need_service.first_name)
        return need_service_form 
    else:
        need_service_form = NeedServeceForm()

    return need_service_form




# SHESTERENKY COUNT
def handle_shesterenky_need_form(request):
    if request.method == 'POST':
        shesterenky_need_form = ShesterenkyNeedForm(request.POST)
        if shesterenky_need_form.is_valid():
            shesterenky_need = WantThisCar(
                year=shesterenky_need_form.cleaned_data['year'],
                vin=shesterenky_need_form.cleaned_data['vin'],
                its_name=shesterenky_need_form.cleaned_data['its_name'],
                img=shesterenky_need_form.cleaned_data['img'],
                first_name=shesterenky_need_form.cleaned_data['first_name'],
                phone=shesterenky_need_form.cleaned_data['phone'],
            )
            shesterenky_need.save()
            shesterenky_need_created.delay(shesterenky_need.first_name)
        return shesterenky_need_form 
    else:
        shesterenky_need_form = ShesterenkyNeedForm()

    return shesterenky_need_form




# KASCO COUNT
def handle_casco_count_form(request):
    if request.method == 'POST':
        casco_count_form = CascoCountForm(request.POST)
        if casco_count_form.is_valid():
            casco_count = WantThisCar(
                budget=casco_count_form.cleaned_data['budget'],
                type=casco_count_form.cleaned_data['type'],
                first_name=casco_count_form.cleaned_data['first_name'],
                phone=casco_count_form.cleaned_data['phone']
            )
            casco_count.save()
            casco_count_created.delay(casco_count.first_name)
        return casco_count_form 
    else:
        casco_count_form = CascoCountForm()

    return casco_count_form




# LEGAL HELP
def handle_legal_help_form(request):
    if request.method == 'POST':
        legal_help_form = LegalHelpForm(request.POST)
        if legal_help_form.is_valid():
            legal_help = WantThisCar(
                where_auto=legal_help_form.cleaned_data['where_auto'],
                documents=legal_help_form.cleaned_data['documents'],
                first_name=legal_help_form.cleaned_data['first_name'],
                phone=legal_help_form.cleaned_data['phone']
            )
            legal_help.save()
            legal_help_created.delay(legal_help.first_name)
        return legal_help_form 
    else:
        legal_help_form = LegalHelpForm()

    return legal_help_form