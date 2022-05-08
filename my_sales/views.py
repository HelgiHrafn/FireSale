from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item
from bid.models import Bid


# Create your views here.
def index(request):
    context = {'items': Item.objects.filter(item_seller_id=request.user.id).order_by('item_name')}
    return render(request, 'my_sales/index.html', context)


def get_item_by_id(request, id):
    highest_bid = get_item_highest_bid(id)
    return render(request, 'my_sales/sell_details.html', {
        'item': get_object_or_404(Item, pk=id),
        'bid': highest_bid
    })


def get_item_highest_bid(id):
    bid = Bid.objects.filter(bid_item_id=id)
    if bid is None:
        return bid
    else:
        bid = bid.order_by('bid_amount').last()
        return bid


def accept_bid(request, id, bid):
    #Do something
    return render(request, 'my_sales/sell_confirm.html')

