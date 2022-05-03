from django.shortcuts import render

sell_items = [
    {'name': 'Jordan skór', 'price': 15000},
    {'name': 'Jordan skór', 'price': 12000},
    {'name': 'Jordan skór', 'price': 15000},
    {'name': 'Jordan skór', 'price': 12000},
    {'name': 'Jordan skór', 'price': 15000},
    {'name': 'Jordan skór', 'price': 15000},
    {'name': 'Jordan skór', 'price': 12000},
    {'name': 'Jordan skór', 'price': 15000},
    {'name': 'Jordan skór', 'price': 12000},
    {'name': 'Jordan skór', 'price': 15000},
]


# Create your views here.
def index(request):
    return render(request, 'firesale/index.html', context={ 'sell_items': sell_items })

