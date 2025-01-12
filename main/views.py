import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse

from cars.models import *
from cars.forms import *
from cars.forms_generator import *
from cars.tasks import * 


def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)
    
def custom_500_view(request):
    return render(request, 'main/500.html', status=500)


# def index_cover(request):
# 	return render(request, 'main/index_cover.html')

def index(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/index.html', context)

def about(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	car_survey_full_form = CarSurveyFullForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'car_survey_full':
			car_survey_full_form = handle_car_survey_full_form(request)

	context = {
		'callme_form': callme_form,
		'car_survey_full_form': car_survey_full_form,

		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/about.html', context)
	
def contact(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/contact.html', context)
	
def guarantee(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	need_diagnostic_form = NeedDiagnosticForm()
	need_service_form = NeedServeceForm()
	guarantee_count_form = GuaranteeCountForm()


	if request.method == 'POST':
		form_type = request.POST.get('form_type')

		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'need_service':
			need_service_form = handle_need_service_form(request)
		elif form_type == 'need_diagnostic':
			need_diagnostic_form = handle_need_diagnostic_form(request)
		elif form_type == 'guarantee_count':	
			guarantee_count_form = handle_guarantee_count_form(request)

	context = {
		'callme_form': callme_form,
		'guarantee_count_form': guarantee_count_form,
		'need_service_form': need_service_form,
		'need_diagnostic_form': need_diagnostic_form,
		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/guarantee.html', context)

def insurance(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	casco_count_form = CascoCountForm()


	if request.method == 'POST':
		form_type = request.POST.get('form_type')

		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'casco_count':
			casco_count_form = handle_casco_count_form(request)


	context = {
		'callme_form': callme_form,
		'casco_count_form': casco_count_form,

		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/insurance.html', context)

def jurists(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	legal_help_form = LegalHelpForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')

		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'legal_help':
			legal_help_form = handle_legal_help_form(request)

	context = {
		'callme_form': callme_form,
		'legal_help_form': legal_help_form,

		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/jurists.html', context)

def privacy(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/privacy.html', context)

def service(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	need_diagnostic_form = NeedDiagnosticForm()
	need_service_form = NeedServeceForm()
	
	if request.method == 'POST':
		form_type = request.POST.get('form_type')

		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'need_service':
			need_service_form = handle_need_service_form(request)
		elif form_type == 'need_diagnostic':
			need_diagnostic_form = handle_need_diagnostic_form(request)

	context = {
		'callme_form': callme_form,
		'need_diagnostic_form': need_diagnostic_form,
		'need_service_form': need_service_form,
		
		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/service.html', context)

def spares(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = CallMeForm()
	shesterenky_need_form = ShesterenkyNeedForm()
	need_diagnostic_form = NeedDiagnosticForm()
	need_service_form = NeedServeceForm()


	if request.method == 'POST':
		form_type = request.POST.get('form_type')

		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'shesterenky_need':
			shesterenky_need_form = handle_shesterenky_need_form(request)
		elif form_type == 'need_service':
			need_service_form = handle_need_service_form(request)
		elif form_type == 'need_diagnostic':
			need_diagnostic_form = handle_need_diagnostic_form(request)

	context = {
		'callme_form': callme_form,
		'shesterenky_need_form': shesterenky_need_form,
		'need_diagnostic_form': need_diagnostic_form,
		'need_service_form': need_service_form,

		'cars': cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/spares.html', context)