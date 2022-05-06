from django.forms import ModelForm, widgets
from firesale.models import Item


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'item_seller']
        widgets = {
            'item_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'item_price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'item_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'item_condition': widgets.Select(attrs={'class': 'form-control'}),
            'item_description': widgets.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'item_name': 'Nafn',
            'item_price': 'Verð',
            'item_image': 'Mynd',
            'item_condition': 'Ástand',
            'item_description': 'Lýsing',
        }
