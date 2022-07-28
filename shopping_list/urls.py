from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Keeps the app urls in the list app.
    path("", include("list.urls")),
    path('admin/', admin.site.urls),
]
