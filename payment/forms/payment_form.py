from django.forms import ModelForm, widgets
from payment.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user', 'payment_item']
        widgets = {
            'card_number': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'exp_month': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'exp_year': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '3'}),
            'name': widgets.TextInput(attrs={'class': 'form-control', 'maxlength': '100'})
        }
        labels = {
            'card_number': 'Kortanúmer',
            'exp_month': 'Mán',
            'exp_year': 'Ár',
            'cvc': 'CVC',
            'name': 'Nafn korthafa'
        }
