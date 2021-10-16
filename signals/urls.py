from django.urls import path
from .views import SignalsListView

app_name = 'signals'

urlpatterns = [
    path('', SignalsListView.as_view(), name='index'),
]