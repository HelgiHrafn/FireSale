from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item
from bid.forms.bid_form import BidCreateForm
from bid.models import Bid
from user.models import Profile

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.item_name,
            'price': x.item_price,
            'firstImage': x.itemimage_set.first().image
        } for x in Item.objects.filter(item_name__icontains=search_filter)]
        return JsonResponse({'data': items})
    # We use exclude to take away items that have an accepted bid so that its no longer for sale
    context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('item_name')}
    return render(request, 'firesale/index.html', context)


def get_item_by_id(request, id):
    # Get highest bid for item
    highest_bid = get_item_highest_bid(id)
    return render(request, 'firesale/item_details.html', {
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
        # In order to create a bid we need to know what item is being bidded on, hence request.path
        bid_item = request.path
        bid_item = bid_item.split('/')
        bid_item = int(bid_item[-2])
        item = Bid(bid_item_id=bid_item)
        form = BidCreateForm()
    return render(request, 'firesale/item_bid.html', {
        'item': item,
        'form': form})
