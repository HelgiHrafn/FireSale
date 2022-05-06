from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_rating']
        widgets = {
            'profile_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_bio': widgets.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'profile_name': 'Nafn',
            'profile_image': 'Mynd',
            'profile_bio': 'Um mig',
        }
