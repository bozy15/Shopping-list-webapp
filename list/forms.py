from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        # specify the model to use
        model = Item
        fields = ["name", "complete"]