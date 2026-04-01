from django import forms
from .models import food_details,restaurant_register

class restaurant_form(forms.ModelForm):
    class Meta:
        model = restaurant_register
        fields = '__all__'


class food_form(forms.ModelForm):
    class Meta:
        model = food_details
        fields = ['foodname','amount','photo']


