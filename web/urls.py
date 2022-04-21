from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', WebIndexView.as_view(), name='index'),
]