from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from payment.forms.payment_form import PaymentForm
from payment.forms.contact_info_form import ContactInfoForm
from firesale.models import Item
from bid.models import Bid
from payment.models import ContactInfo, Payment, OrderInfo
from payment.forms.Order_info_form import OrderForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    return render(request, 'payment/payment.html')


def payment(request, item_id):
    item = Item.objects.get(id=item_id)
    payment_object_old = Payment.objects.filter(payment_item_id=item_id).first()
    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            payment_object = form.save(commit=False)
            user_id = request.user.id
            payment_object.user_id = user_id
            payment_object.payment_item_id = item_id
            if not payment_object_old:
                payment_object.save()
            else:
                payment_object.id = payment_object_old.id
                payment_object.save()
            # pay_info.save() # ATHHHHHHHHHHHH
            return redirect('payment-review', item_id)
    else:
        form = PaymentForm(instance=payment_object_old)
        item = Item.objects.get(id=item_id)
        bid = Bid.objects.filter(bid_item_id=item.id).get(bid_status=True)
    return render(request, 'payment/payment.html', {
        'form': form,
        'item': item,
        'bid': bid
    })


def contact_info(request, bid_id):
    bid = Bid.objects.get(id=bid_id)
    item_id = bid.bid_item_id
    contact_object_old = ContactInfo.objects.filter(payment_item_id=item_id).first()
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            contact_object = form.save(commit=False)
            user_id = request.user.id
            contact_object.user_id = user_id
            contact_object.payment_item_id = item_id
            if not contact_object_old:
                contact_object.save()
            else:
                contact_object.id = contact_object_old.id
                contact_object.save()
            return redirect('payment-payment', item_id)
    else:
        form = ContactInfoForm(instance=contact_object_old)
        bid = Bid.objects.get(id=bid_id)
    return render(request, 'payment/contact_info.html', {
        'form': form,
        'bid': bid,

    })


def review(request, item_id):
    contact_review = ContactInfo.objects.get(payment_item_id=item_id)
    payment_review = Payment.objects.get(payment_item_id=item_id)
    item = Item.objects.get(id=item_id)
    bid = Bid.objects.filter(bid_status=True).get(bid_item_id=item.id)
    return render(request, 'payment/review.html', {
        'contact': contact_review,
        'payment': payment_review,
        'item_id': item,
        'bid': bid

    })


def payment_processed(request, item_id):
    item = Item.objects.get(id=item_id)
    bid = Bid.objects.get(bid_item_id=item.id, bid_status=True)
    bid.bid_paid = True
    bid.save()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            order_object = form.save(commit=False)
            order_object_old = OrderInfo.objects.filter(item_id=item_id).first()
            order_object_old.rating = order_object.rating
            order_object_old.save()
            return redirect('firesale-index')
    else:
        order = OrderInfo(seller_id=item.item_seller.id, buyer_id=bid.user_id, item_id=item.id)
        order.save()
    return render(request, 'payment/payment_processed.html', {
        'form': OrderForm(),
        'item_id': item
    })
