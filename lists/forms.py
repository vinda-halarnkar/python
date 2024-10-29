from django import forms
from .models import List, Item

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name']

class ItemForm(forms.ModelForm):
    color = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'color'}),
        required=False,  # Make it optional if you want
    )
    class Meta:
        model = Item
        fields = ['name', 'color']
