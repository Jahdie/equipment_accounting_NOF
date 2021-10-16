from django.urls import path
from .views import signals

app_name = 'signals'

urlpatterns = [
    path('', signals, name='index'),
]