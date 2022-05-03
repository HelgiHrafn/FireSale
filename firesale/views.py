from django.shortcuts import render
from firesale.models import Item
from firesale.models import Condition

sell_items = [
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 500},
    {'name': 'Jordan skór', 'price': 12000, 'highestbid': 0},
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 1850},
    {'name': 'Jordan skór', 'price': 12000, 'highestbid': 2500},
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 250},
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 5000},
    {'name': 'Jordan skór', 'price': 12000, 'highestbid': 0},
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 0},
    {'name': 'Jordan skór', 'price': 12000, 'highestbid': 8000},
    {'name': 'Jordan skór', 'price': 15000, 'highestbid': 500},
]


# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('item_name')}
    return render(request, 'firesale/index.html', context)

