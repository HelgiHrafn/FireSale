from django.forms import ModelForm, widgets
from payment.models import OrderInfo


class OrderForm(ModelForm):
    class Meta:
        model = OrderInfo
        exclude = ['id', 'buyer', 'seller', 'item']
        widgets = {
            'rating': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '1'}),
        }
        labels = {
            'rating': 'Stjörnur',
        }