from django.shortcuts import render

# Home page view to display the list of items.
def index(request):
    return render(request, "list/shopping_list.html")

# View to add an item to the list
def add_item(request):
    return render(request, "list/add_item.html")