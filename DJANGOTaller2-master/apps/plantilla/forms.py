from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})




class NameForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name','size':12}))
    country = forms.CharField( max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country','size':12}))
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())

