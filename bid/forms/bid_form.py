from django.forms import ModelForm, widgets
from bid.models import Bid


class BidCreateForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'bid_status', 'bid_item', 'user', 'bid_paid']
        widgets = {
            'bid_amount': widgets.NumberInput(attrs={'class': 'form-control', 'maxlength': '9'}),
        }
        labels = {
            'bid_amount': 'Upphæð'
        }
