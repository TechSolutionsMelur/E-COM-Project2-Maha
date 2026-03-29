from django import forms
from .models import food_details,register_models

class food_form(forms.ModelForm):
    class Meta:
        model = food_details
        fields = ['foodname','amount','photo']

class register_form(forms.ModelForm):
    class Meta:
        model = register_models
        fields = ['restaurant_name','location']