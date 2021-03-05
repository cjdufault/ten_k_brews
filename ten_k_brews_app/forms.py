from django import forms
from .models import Drink


class EstablishmentSearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=100)


class NewDrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'type', 'style', 'description')
