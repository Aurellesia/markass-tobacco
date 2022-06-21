from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email
from django.forms import ModelForm, PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(validators=[RegexValidator('^[a-zA-Z0-9\_\-\@\.\+\-]*$', message="Username hanya huruf atau angka")])
    password = forms.CharField(widget=PasswordInput)