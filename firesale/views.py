from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from firesale.models import Item, ItemCategory
from bid.forms.bid_form import BidCreateForm
from bid.models import Bid
from user.models import Profile


# Create your views here.
def index(request, opt=None):
    print(opt)
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.item_name,
            'price': x.item_price,
            'firstImage': x.itemimage_set.first().image
        } for x in Item.objects.filter(item_name__icontains=search_filter)]
        return JsonResponse({'data': items})
    if opt == 'cheap':
        context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('item_price')}
    elif opt == 'exp':
        context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('-item_price')}
    elif opt == 'alp':
        context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('item_name')}
    elif opt == 'rev':
        context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('-item_name')}
    else:
        context = {'items': Item.objects.exclude(bid__bid_status=True).all().order_by('-id')}

    return render(request, 'firesale/index.html', context)


def get_item_by_id(request, id):
    # Get highest bid for item
    highest_bid = get_item_highest_bid(id)
    items = get_category_items(id).order_by('?')[:5]
    #items2 = Item.objects.exclude(bid__bid_status=True).all().order_by('item_name')
    return render(request, 'firesale/item_details.html', {
        'item': get_object_or_404(Item, pk=id),
        'bid': highest_bid,
        'items': items,

    })


def get_category_items(id):
    item = Item.objects.get(id=id)
    category = item.item_category
    items_same_category = Item.objects.filter(item_category=category).exclude(bid__bid_status=True).exclude(id=id)
    return items_same_category


def get_item_highest_bid(id):
    bid = Bid.objects.filter(bid_item_id=id)
    if bid is None:
        return bid
    else:
        bid = bid.order_by('bid_amount').last()
        return bid


@login_required
def bid_item_by_id(request, id):
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
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
