from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.urls import reverse

app_name = 'main'


urlpatterns = [

    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('guarantee/', views.guarantee, name = 'guarantee'),
    path('insurance/', views.insurance, name = 'insurance'),
    path('jurists/', views.jurists, name = 'jurists'),
    path('privacy/', views.privacy, name = 'privacy'),
    path('service/', views.service, name = 'service'),
    path('spares/', views.spares, name = 'spares'),

]