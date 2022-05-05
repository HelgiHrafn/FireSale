from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'rating']
        widgets = {
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name:': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name:': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.PasswordInput(attrs={'class': 'form-control'}),
 }


