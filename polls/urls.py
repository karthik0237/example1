from django.urls import path
from . import views

urlpatterns = [
    path('polls1',views.index1, name = "index1"),
    path('polls2',views.index2, name = "index2"),
]