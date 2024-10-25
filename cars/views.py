import os
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.conf import settings

from .models import *
from .forms import *
from .forms_generator import *
from .filters import *


def catalog(request):
	sort_by = request.GET.get('sort_by', 'asc')
	
	# form = FilterForm(request.GET or None)

	cars = Car.objects.all()

	products_list = Car.objects.all()
	products_list = cars_ordering(Car, products_list, sort_by)

	queryset = products_list


	if request.method == 'GET':
		queryset = cars_filtering(request, queryset)
		print(queryset)


	unique_values = unique_names(request)

	
	status = request.GET.get('status')
	if status:
		status = int(status)
		cars = cars.filter(status=status)



	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
		'products_list': products_list,
		'queryset': queryset,
		'unique_color': unique_values['unique_color'],
		'unique_year': unique_values['unique_year'],
		'unique_transmission': unique_values['unique_transmission'],
		'unique_drive': unique_values['unique_drive'],
	}

	return render(request, 'cars/catalog.html', context)




def fresh_cars(request):
	sort_by = request.GET.get('sort_by', 'asc')
	cars = Car.objects.filter(status=1)
	cars = cars_ordering(Car, cars, sort_by)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()


	context = {
		'cars' : cars,
		'callme_form': callme_form,
	}

	return render(request, 'cars/fresh.html', context)



def used_cars(request):
	sort_by = request.GET.get('sort_by', 'asc')
	cars = Car.objects.filter(status=2)	
	cars = cars_ordering(Car, cars, sort_by)

	if request.method == 'POST':
		callme_form = CallMeForm(request.POST)
		if callme_form.is_valid():
			callme = callme_form.save()
			send_email_task.delay(callme.first_name)
	else:
		callme_form = CallMeForm()

	context = {
		'cars':cars,
		'callme_form': callme_form,
	}

	return render(request, 'cars/used.html', context)




def the_car(request, id):		
	if id:
		the_car = get_object_or_404(Car, id=id)
		similar_cars = Car.objects.filter(category=the_car.category)
		new_cars = Car.objects.filter(status=1)
		used_cars = Car.objects.filter(status=2)
	
	callme_form = handle_callme_form(request)
	want_this_car = handle_want_this_car_form(request)

	context = {
		'the_car': the_car,
		# 'sort_by': sort_by,
		'similar_cars': similar_cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
		'callme_form': callme_form,
		'want_this_car': want_this_car,
	}
	return render(request, 'cars/the_car.html', context)