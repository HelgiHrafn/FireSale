from django.db import models
from django.contrib.auth.models import User
from firesale.models import Item


# Create your models here.
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.BigIntegerField(max_length=9)
    bid_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bid_status = models.BooleanField(default=False)
    bid_paid = models.BooleanField(default=False)
