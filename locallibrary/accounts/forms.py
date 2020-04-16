from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """ Extending the UserCreationForm """
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter first name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter Last name')
    email = forms.EmailField(max_length=254, help_text='Required and will send verification')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
