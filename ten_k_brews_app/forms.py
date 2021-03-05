from django import forms
from .models import Drink


class NewDrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'type', 'style', 'description')
