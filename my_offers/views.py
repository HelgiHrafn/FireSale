from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from bid.models import Bid
from firesale.models import Item


# Create your views here.
def index(request):
    context = {'bids': Bid.objects.filter(user_id=request.user.id).exclude(bid_paid=True).order_by('bid_status'),
               'items': Item.objects.all()}
    return render(request, 'my_offers/index.html', context)


def get_item_for_bid(request, id):
    return render(request, 'my_offers/offer_details.html', {
        'bid': get_object_or_404(Bid, pk=id )
    })

