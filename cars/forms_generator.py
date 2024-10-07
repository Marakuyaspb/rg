from order.forms import *
from order.models import *
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
            want_this_car = WantThisCarForm(
                first_name=want_this_car_form.cleaned_data['first_name'],
                phone=want_this_car_form.cleaned_data['phone']
            )
            want_this_car.save()
            want_this_car_created.delay(want_this_car.first_name)
        return want_this_car_form 
    else:
        want_this_car_form = WantThisCarForm()

    return want_this_car_form




# CAR SURVEY FULL
def handle_survey_full_form(request):
    pass

# GUARANTEE COUNT
def handle_guarantee_count_form(request):
    pass

# NEED DIAGNOSTIC
def handle_need_diagnostic_form(request):
    pass

# NEED SERVICE
def handle_need_service_form(request):
    pass

# SHESTERENKY COUNT
def handle_shesterenky_need_form(request):
    pass

# KASCO COUNT
def handle_casco_count_form(request):
    pass

# LEGAL HELP
def handle_legal_help_form(request):
    pass