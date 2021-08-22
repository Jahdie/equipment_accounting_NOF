"""equipment_accounting_NOF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from locations.views import locations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locations, name='index'),
    path('locations/', include('locations.urls', namespace='locations')),
    path('technical_equipments/', include('technical_equipments.urls', namespace='technical_equipments')),
    path('switch_cabinets/', include('switch_cabinets.urls', namespace='switch_cabinets')),
    path('signals/', include('signals.urls', namespace='signals')),
    path('factory_equipments/', include('factory_equipments.urls', namespace='factory_equipment')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
