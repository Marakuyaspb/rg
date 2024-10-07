from order.forms import *
from .models import *
from order.tasks import callme_created 


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
    pass

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