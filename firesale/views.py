from django.shortcuts import render

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
    return render(request, 'firesale/index.html', context={ 'sell_items': sell_items })

