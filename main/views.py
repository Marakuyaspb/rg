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



def index(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/index.html', context)


def feedback(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/feedback.html', context)


def guarantee(request):
	cars = Car.objects.all()

	used_cars = Car.objects.filter(status=2)

	callme_form = handle_callme_form(request)
	guarantee_count_form = handle_guarantee_count_form(request)

	context = {
		'callme_form': callme_form,
		'guarantee_count_form': guarantee_count_form,
		'cars' : cars,
		'used_cars': used_cars
	}
	return render(request, 'main/guarantee.html', context)


def insurance(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)
	casco_count_form = handle_casco_count_form(request)

	context = {
		'callme_form': callme_form,
		'casco_count_form': casco_count_form,
		'cars' : cars,
	}
	return render(request, 'main/insurance.html', context)


def jurists(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)
	legal_help_form = handle_legal_help_form(request)

	context = {
		'callme_form': callme_form,
		'legal_help_form': legal_help_form,
		'cars' : cars,
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

	callme_form = handle_callme_form(request)
	need_diagnostic_form = handle_need_diagnostic_form(request)
	need_service_form = handle_need_service_form(request)
	guarantee_count_form = handle_guarantee_count_form(request)

	context = {
		'callme_form': callme_form,
		'need_diagnostic_form': need_diagnostic_form,
		'need_service_form': need_service_form,
		'guarantee_count_form': guarantee_count_form,
		
		'cars' : cars,
	}
	return render(request, 'main/service.html', context)


def spares(request):
	cars = Car.objects.all()

	callme_form = handle_callme_form(request)
	shesterenky_need_form = handle_shesterenky_need_form(request)
	need_diagnostic_form = handle_need_diagnostic_form(request)
	need_service_form = handle_need_service_form(request)

	context = {
		'callme_form': callme_form,
		'shesterenky_need_form': shesterenky_need_form,
		'need_diagnostic_form': need_diagnostic_form,
		'need_service_form': need_service_form,
		'cars' : cars,
	}
	return render(request, 'main/spares.html', context)