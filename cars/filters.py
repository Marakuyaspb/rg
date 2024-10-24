from django.db.models import Count, Q
from .models import *

def cars_ordering(instance, queryset, sort_by):
	if sort_by == 'asc':
		return queryset.order_by('price')
	elif sort_by == 'desc':
		return queryset.order_by('-price')
	else:
		return queryset


def cars_filtering(request, queryset):
	filters = Q()

	color_ids = request.GET.getlist('color_id')
	years = request.GET.getlist('year')
	drives = request.GET.getlist('drive')
	transmissions = request.GET.getlist('transmission')

	if color_ids:
		filters &= Q(color_id__in=color_ids)
	if years:
		filters &= Q(year=years)
	if transmissions:
		filters &= Q(transmission=transmissions)
	if drives:
		filters &= Q(drive=drives)

	return queryset.filter(filters)



def unique_names(request):
	unique_color = Color.objects.values('color_name', 'color_id', 'color_code').distinct()
	unique_year = Car.objects.values('year').annotate(total=Count('year')).order_by('year').distinct()
	unique_transmission = Car.objects.values('transmission').annotate(total=Count('transmission')).order_by('transmission').distinct()
	unique_drive = Car.objects.values('drive').annotate(total=Count('drive')).order_by('drive').distinct()

	return {
		'unique_color': unique_color,
		'unique_year': unique_year,
		'unique_drive': unique_drive,
		'unique_transmission': unique_transmission,
	}
