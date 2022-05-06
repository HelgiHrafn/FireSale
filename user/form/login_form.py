"""from django.contrib.auth.forms import UserCreationForm,
from django.forms import widgets

from user.models import Profile

class LoginForm(UserCreationForm):
    class Meta:
        model = Profile
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'})
            'password': widgets.TextInput(attrs={'class': 'form-control'})
        }
"""