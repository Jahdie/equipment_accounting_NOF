from django.urls import path
from .views import StationsListView

app_name = 'signals'

urlpatterns = [
    path('', StationsListView, name='index'),
]