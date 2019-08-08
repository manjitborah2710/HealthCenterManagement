from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignInForm(forms.Form):
    DOCTOR = 'DR'
    PATIENT = 'PT'
    STOCK_MAN = 'SM'
    ADMIN = 'AD'
    SIGN_IN_CHOICES =  (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
        (STOCK_MAN, 'Stock_Manager'),
        (ADMIN, 'Administrator')
    )
    sign_in_as = forms.ChoiceField(choices = SIGN_IN_CHOICES)
    username = forms.CharField(label='Username', max_length=10)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
