from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item
from bid.models import Bid
from django.core.mail import send_mail
from django.contrib.auth.models import User
from user.models import Profile


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
    print(item)
    print(id)
    print(bid.id)
    bid.bid_status = True
    bid.save()
    send_email_to_buyer(item.item_name, bid.user_id)
    return render(request, 'my_sales/sell_confirm.html')


def send_email_to_buyer(name, id):
    profile = Profile.objects.get(user_id=id)
    send_mail('FIRESALE: Tilboð samþykkt',
              'Tilboð í vöru '+name+' hefur verið samþykkt. Skráðu þig inn til að ganga frá greiðslu.',
              'kristjanm20@ru.is',
              [profile.profile_email],
              fail_silently=True,
              )
