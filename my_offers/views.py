from django.shortcuts import render
from bid.models import Bid


# Create your views here.
def index(request):
    context = {'items': Bid.objects.filter(user_id=request.user.id).order_by('bid_status')}
    return render(request, 'my_offers/index.html', context)
