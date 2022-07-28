from django.shortcuts import render
from django.http import HttpResponse

# Test view for the shopping list app.
def index(request):
    return HttpResponse("Hello, world. You're at the shopping list index.")