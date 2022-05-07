
from django.shortcuts import render, get_object_or_404, redirect


from bid.forms.bid_form import BidCreateForm
from bid.models import Bid


def make_bid(request):
    if request.method == 'GET':
        return render(request, 'bid/bid_item.html', {
            'bid': id})


def make_bid2(request):
    result = request.POST.get("bid")
    print(result)
    if request.method == 'POST':
        form = BidCreateForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            amount = form.cleaned_data.get("bid_amount")
            user = request.user.id
            bid_item = request.item.id
            form = Bid(bid_amount=amount, user_id=user, bid_item_id=bid_item)
            form.save()
            return redirect('profile')
    return render(request, 'bid/bid_item.html')


