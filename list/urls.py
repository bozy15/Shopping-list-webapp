from django.urls import path
from list import views

urlpatterns = [
    path("", views.index, name="index"),
]