from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
	path('admin/order/carsurveyfull/<int:id>/', views.admin_carSurveyFull_detail, name='admin_carSurveyFull_detail'),
]