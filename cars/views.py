import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings

from .models import Category, Status, Car
from .forms_generator import handle_callme_form, handle_want_this_car_form, handle_survey_full_form, handle_guarantee_count_form, handle_need_diagnostic_form, handle_need_service_form, handle_shesterenky_need_form, handle_casco_count_form, handle_legal_help_form


def catalog(request):
	cars = Car.objects.all()
	
	status = request.GET.get('status')
	if status:
		status = int(status)
		cars = cars.filter(status=status)

	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}

	return render(request, 'cars/catalog.html', context)


def fresh_cars(request):
	cars = Cars.objects.filter(status=1)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}

	return render(request, 'cars/fresh.html', context)


def used_cars(request):
	cars = Cars.objects.filter(status=2)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}

	return render(request, 'cars/used.html', context)



def the_car(request, id):		
	if id:
		the_car = get_object_or_404(Car, id=id)
		similar_cars = Car.objects.filter(category=the_car.category)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'the_car': the_car,
		'similar_cars': similar_cars,
		'callme_form': callme_form
	}
	return render(request, 'cars/the_car.html', context)