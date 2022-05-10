from django.shortcuts import render, redirect
from payment.forms.payment_form import PaymentForm
from payment.forms.contact_info_form import ContactInfoForm
from firesale.models import Item


# Create your views here.
def index(request):
    return render(request, 'payment/payment.html')


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            pay_info = form.save(commit=False)
            pay_info.user = request.user
            # pay_info.save() # ATHHHHHHHHHHHH
            print("payment success")  # ATHHHHHHHHHHHHH
            return redirect('my_offers-index')
    else:
        form = PaymentForm()
    return render(request, 'payment/payment.html', {
        'form': form
    })


def contact_info(request):
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            # info.save() # ATHHHHHHHHHHHHHHHHHHhh
            print("contact info success")  # ATHHHHHHHHHHHHH
            return redirect('payment-payment')
    else:
        form = ContactInfoForm()
    return render(request, 'payment/contact_info.html', {
        'form': form
    })


def review(request):
    return render(request, 'payment/review.html')