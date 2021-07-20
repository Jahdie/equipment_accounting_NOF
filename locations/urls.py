from django.urls import path
from .views import LocationsListView

app_name = 'locations'

urlpatterns = [
    path('', LocationsListView.as_view(), name='index'),
]