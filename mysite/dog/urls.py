from django.urls import path

from . import views

urlpatterns = [
    path('doggy', views.index, name = 'doggy')
]
