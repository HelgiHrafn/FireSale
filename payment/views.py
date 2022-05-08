from django.shortcuts import render
from payment.forms.payment_form import Payment
from firesale.models import Item

# Create your views here.
def index(request):
    return render(request, 'payment/index.html')

def payment(request):
    if request.method == 'POST':
        form = Payment(data=request.POST)
        if form.is_valid():
            card_number = form.cleaned_data.get("card_number")


