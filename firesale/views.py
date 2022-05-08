from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item
from bid.forms.bid_form import BidCreateForm
from bid.models import Bid


# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('item_name')}
    return render(request, 'firesale/index.html', context)


def get_item_by_id(request, id):
    highest_bid = get_item_highest_bid(id)
    return render(request, 'firesale/item_details.html', {
        'item': get_object_or_404(Item, pk=id),
        'bid': highest_bid
    })


def get_item_highest_bid(id):
    bid = Bid.objects.filter(bid_item_id=id)
    bid = bid.order_by('bid_amount').last()
    return bid


def bid_item_by_id(request, id):
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            amount = form.cleaned_data.get("bid_amount")
            user = request.user.id
            bid_item = id
            form = Bid(bid_amount=amount, user_id=user, bid_item_id=bid_item)
            form.save()
            return redirect('firesale-index')
    else:
        bid_item = request.path
        bid_item = int(bid_item[-2])
        item = Bid(bid_item_id=bid_item)
        form = BidCreateForm()
    return render(request, 'firesale/item_bid.html', {
        'item': item,
        'form': form})
