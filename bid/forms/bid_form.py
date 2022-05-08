from django.forms import ModelForm, widgets
from bid.models import Bid


class BidCreateForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'bid_status', 'bid_item', 'user']
        widgets = {
            'bid_amount': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'bid_amount': 'Upphæð'
        }
