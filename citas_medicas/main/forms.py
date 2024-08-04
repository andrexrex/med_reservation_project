from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    customer_name = forms.CharField(max_length=64)
    customer_email = forms.EmailField()
    customer_phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')