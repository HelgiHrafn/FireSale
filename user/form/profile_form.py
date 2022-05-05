from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_rating']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
        }


