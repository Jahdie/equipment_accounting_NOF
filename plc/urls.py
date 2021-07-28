from django.urls import path
from .views import PLCListView

app_name = 'signals'

urlpatterns = [
    path('', PLCListView, name='index'),
]