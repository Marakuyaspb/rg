import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings

from .models import Category, Status, Car, CallMe
from .forms import CallMeForm


def catalog(request):
	cars = Cars.objects.all()
	
	category = request.GET.get('category')
	if category:
		category = int(category)
		if category == 1:
			cars = Cars.objects.filter(category=1)
		elif category == 2:
			cars = Cars.objects.filter(category=2)
		elif category == 2:
			cars = Cars.objects.filter(category=3)
	
	status = request.GET.get('status')
	if status:
		status = int(status)
		if status == 1:
			cars = Cars.objects.filter(status=1)
		elif status == 2:
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

	return render(request, 'cars/catalog.html')


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



def the_car(request, category=None, id=None):		
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
		'similar_cars': similar_cases,
		'callme_form': callme_form
	}
	return render(request, 'cars/the_car.html', context)