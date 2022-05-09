from django.forms import ModelForm, widgets
from payment.models import ContactInfo


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ['id', 'user', 'payment_item']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'post_code': widgets.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': 'Fornafn',
            'last_name': 'Eftirnafn',
            'street_name': 'Götuheiti',
            'street_number': 'Húsnúmer',
            'city': 'Bæjarfélag',
            'post_code': 'Póstnúmer'
        }
