from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from django.conf.urls import handler404, handler500
from .views import custom_404_view, custom_500_view

from main import urls
from cars import urls



admin.site.site_header = 'Система Централизованного Управления Контентом'

handler404 = custom_404_view
handler500 = custom_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
    path('', include('main.urls')),
]


urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)