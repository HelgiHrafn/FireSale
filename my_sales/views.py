from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item
from bid.models import Bid
from django.core.mail import send_mail
from django.contrib.auth.models import User


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
    item = Item.objects.get(id=id)
    bid = Bid.objects.get(id=bid)
    bid.bid_status = True
    bid.save()
    send_email(item.name, bid.id)


    send_mail('Tilboð samþykkt',
              'Hello hello',
              'kristjanm20@ru.is',
              ['bid.bid'],
              fail_silently=False,
              )
        #Do something
    return render(request, 'my_sales/sell_confirm.html')


def send_email(name, id):
    user = User.objects.get(id=id)
    send_mail('Tilboð samþykkt',
              'Hello hello',
              'kristjanm20@ru.is',
              ['user.em'],
              fail_silently=False,
              )
