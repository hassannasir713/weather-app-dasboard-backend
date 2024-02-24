from django import forms
from .models import FavouriteCity

class FavouriteCityForm(forms.ModelForm):
    class Meta:
        model = FavouriteCity
        fields = ('city',)