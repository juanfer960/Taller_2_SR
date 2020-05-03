from django import forms
from django.core import validators
from .models import User


class FormName(forms.Form):
    name = forms.CharField()
    password = forms.CharField()


    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['name']
        password = all_clean_data['password']


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'


class FormSearch(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2','type' : 'text', 'aria-label' : 'Search'}))
    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['search']
