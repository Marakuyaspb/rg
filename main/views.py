import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse


from cars.models import Category, Status, Car, CallMe
from cars.forms import CallMeForm

def index(request):
	return render(request, 'main/index.html')

def feedback(request):
	return render(request, 'main/feedback.html')

def guarantee(request):
	return render(request, 'main/guarantee.html')

def insurance(request):
	return render(request, 'main/insurance.html')

def jurists(request):
	return render(request, 'main/jurists.html')

def privacy(request):
	return render(request, 'main/privacy.html')

def service(request):
	return render(request, 'main/service.html')

def spares(request):
	return render(request, 'main/spares.html')