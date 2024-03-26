from django.urls import path
from . import views

urlpatterns = [
    path("survey", views.f1, name = 'f1'),
]