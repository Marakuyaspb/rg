import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse

from cars.models import Category, Status, Car, CallMe
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
	return render(request, 'main/guarantee.html', context)


def insurance(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/insurance.html', context)


def jurists(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
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

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/service.html', context)


def spares(request):
	cars = Car.objects.all()
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
	}
	return render(request, 'main/spares.html', context)