from django.db import models
from django.contrib.auth.models import User
from firesale.models import Item


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    name = models.TextField()
