# project/context_processors.py
from user.models import Profile
from django.db.models import Avg
from payment.models import OrderInfo
from user.models import Profile


def user_rating(request):
    user_id = request.user.id
    print(user_id)
    print("hello")
    try:
        print("helllll")
        orders = OrderInfo.objects.filter(seller_id=user_id).aggregate(Avg('rating'))
        rating = list(orders.values())[0]
        rating = int(rating)
        print(rating)

        return {'rating__avg': rating}
    except:
        return {'rating__avg': 0}



