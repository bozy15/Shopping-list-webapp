from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Home page view to display the list of items.
def index(request):
    # Get all items from the database
    items = Item.objects.all()
    # Render the template with the items
    context = {"items": items}
    return render(request, "list/shopping_list.html", context)


# View to add an item to the list
def add_item(request):
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = ItemForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # Save the new item to the database
            # and redirect to the list page
            form.save()
            return redirect(index)
    # Create an instance of the form
    # and render it to the template
    form = ItemForm()
    context = {"form": form}
    return render(request, "list/add_item.html", context)


# View to edit an item in the list
def edit_item(request, item_id):
    # Get item or return 404 error
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = ItemForm(request.POST, instance=item)
        # Check if the form is valid:
        if form.is_valid():
            # Save the new item to the database
            # and redirect to the list page
            form.save()
            return redirect(index)
    # Create an instance of the form
    # and render it to the template
    form = ItemForm(instance=item)
    context = {"form": form}
    return render(request, "list/edit_item.html", context)

# View to toggle an item's "completed" status
def toggle_item(request, item_id):
    # Get item or return 404 error
    item = get_object_or_404(Item, id=item_id)
    # Toggle the item's "completed" status
    item.complete = not item.complete
    item.save()
    # Redirect to the list page
    return redirect(index)