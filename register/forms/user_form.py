from django.forms import ModelForm, widgets
from login.models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name:': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name:': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'user_name': 'Notendanafn',
            'first_name': 'Fornafn',
            'last_name': 'Eftirnafn',
            'email': 'Netfang',
            'password': 'Lykilorð'
        }


