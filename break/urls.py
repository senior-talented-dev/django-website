from django.urls import path

from . import views

app_name = 'break'

urlpatterns = [
    path('', views.home, name='index'),
]