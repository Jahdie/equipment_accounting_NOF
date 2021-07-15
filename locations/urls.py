from django.urls import path
from .views import LocationsListView

app_name = 'locations'

urlpatterns = [
    path('', LocationsListView, name='index'),
]