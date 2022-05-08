from django.forms import ModelForm, widgets
from payment.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user', 'payment_item']
        widgets = {
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'card_number': 'Kortanúmer',
            'exp_month': 'Mán',
            'exp_year': 'Ár',
            'cvc': 'CVC',
            'name': 'Nafn korthafa'
        }
