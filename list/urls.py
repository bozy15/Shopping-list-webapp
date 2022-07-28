from django.urls import path
from list import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_item", views.add_item, name="add_item"),
    path("edit_item/<item_id>", views.edit_item, name="edit_item"),
    path("toggle_item/<item_id>", views.toggle_item, name="toggle_item"),
    path("delete_item/<item_id>", views.delete_item, name="delete_item"),
    path("delete_all", views.delete_all, name="delete_all"),
]