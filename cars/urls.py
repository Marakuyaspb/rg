from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars import views
from django.urls import reverse

app_name = 'cars'


urlpatterns = [
    path('catalog/', views.catalog, name = 'catalog'),
    path('fresh/', views.fresh_cars, name = 'fresh_cars'),
    path('used/', views.used_cars, name = 'used_cars'),
]