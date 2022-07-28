from django.urls import path
from list import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_item", views.add_item, name="add_item"),
]