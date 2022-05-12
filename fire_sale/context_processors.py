# project/context_processors.py
from user.models import Profile
from django.db.models import Avg
from payment.models import OrderInfo
from user.models import Profile


def user_rating(request):
    user_id = request.user.id
    print("hello")
    try:
        orders = OrderInfo.objects.filter(seller_id=user_id)
    except:
        orders =None



    profile_imgaa = Profile.objects.all()[:1].get()
    return {'profile_imageaa': profile_imgaa}