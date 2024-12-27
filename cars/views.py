import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F, Count, Value
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template

from .models import *
from .forms import *
from .forms_generator import *
from .filters import *
from .tasks import * 


def catalog(request):
	cars = Car.objects.all()
	queryset = cars

	if request.method == 'GET':
		filtered_queryset = cars_filtering(request, queryset)
		print(filtered_queryset)
		if filtered_queryset.exists():
			queryset = filtered_queryset
		else:
			queryset = None

	unique_values = unique_names(request)

	status = request.GET.get('status')
	if status:
		status = int(status)
		cars = cars.filter(status=status)


	callme_form = CallMeForm()
	car_survey_full_form = CarSurveyFullForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'car_survey_full':
			car_survey_full_form = handle_car_survey_full_form(request)

	context = {
		'cars' : cars,
		'queryset': queryset,
		'unique_brand': unique_values['unique_brand'],
		'unique_color': unique_values['unique_color'],
		'unique_year': unique_values['unique_year'],
		'unique_transmission': unique_values['unique_transmission'],
		'unique_drive': unique_values['unique_drive'],

		'callme_form': callme_form,
		'car_survey_full_form': car_survey_full_form
	}

	return render(request, 'cars/catalog.html', context)



def fresh_cars(request):
	sort_by = request.GET.get('sort_by', 'asc')
	cars = Car.objects.filter(status=1)
	cars = cars_ordering(Car, cars, sort_by)
	used_cars = Car.objects.filter(status=2)

	queryset = cars
	
	if request.method == 'GET':
		filtered_queryset = cars_filtering(request, queryset)
		print(filtered_queryset)
		if filtered_queryset.exists():
			queryset = filtered_queryset
		else:
			queryset = None
	unique_values = unique_names(request)


	callme_form = CallMeForm()
	car_survey_full_form = CarSurveyFullForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'car_survey_full':
			car_survey_full_form = handle_car_survey_full_form(request)

	context = {
		'cars' : cars,
		'used_cars': used_cars,
		'queryset': queryset,
		'unique_brand': unique_values['unique_brand'],
		'unique_color': unique_values['unique_color'],
		'unique_year': unique_values['unique_year'],
		'unique_transmission': unique_values['unique_transmission'],
		'unique_drive': unique_values['unique_drive'],

		'callme_form': callme_form,
		'car_survey_full_form': car_survey_full_form
	}

	return render(request, 'cars/fresh.html', context)



def used_cars(request):
	sort_by = request.GET.get('sort_by', 'asc')
	cars = Car.objects.filter(status=2)	
	cars = cars_ordering(Car, cars, sort_by)
	new_cars = Car.objects.filter(status=1)

	queryset = cars
	if request.method == 'GET':
		filtered_queryset = cars_filtering(request, queryset)
		print(filtered_queryset)
		if filtered_queryset.exists():
			queryset = filtered_queryset
		else:
			queryset = None
	unique_values = unique_names(request)


	callme_form = CallMeForm()
	car_survey_full_form = CarSurveyFullForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'car_survey_full':
			car_survey_full_form = handle_car_survey_full_form(request)


	context = {
		'cars':cars,
		'new_cars': new_cars,
		'queryset': queryset,
		'unique_brand': unique_values['unique_brand'],
		'unique_color': unique_values['unique_color'],
		'unique_year': unique_values['unique_year'],
		'unique_transmission': unique_values['unique_transmission'],
		'unique_drive': unique_values['unique_drive'],

		'callme_form': callme_form,
		'car_survey_full_form': car_survey_full_form
	}

	return render(request, 'cars/used.html', context)



def the_car(request, id):		
	if id:
		the_car = get_object_or_404(Car, id=id)
		similar_cars = Car.objects.filter(category=the_car.category)
		new_cars = Car.objects.filter(status=1)
		used_cars = Car.objects.filter(status=2)


	callme_form = CallMeForm()
	want_this_car_form = WantThisCarForm()
	car_survey_full_form = CarSurveyFullForm()
	casco_count_form = CascoCountForm()
	
	want_this_car = None

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'want_this_car':
			want_this_car = handle_want_this_car_form(request)
			print(want_this_car_form.errors) 
		elif form_type == 'car_survey_full':
			car_survey_full_form = handle_car_survey_full_form(request)
		elif form_type == 'casco_count':
			casco_count_form = handle_casco_count_form(request)


	context = {
		'the_car': the_car,
		'similar_cars': similar_cars,
		'new_cars': new_cars,
		'used_cars': used_cars,

		'callme_form': callme_form,
		'want_this_car_form': want_this_car_form,
		'car_survey_full_form': car_survey_full_form,
		'casco_count_form': casco_count_form
	}
	return render(request, 'cars/the_car.html', context)