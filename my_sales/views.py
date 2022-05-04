from django.shortcuts import render
from firesale.models import Item

# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('item_name')}
    return render(request, 'my_sales/index.html', context)
