from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from firesale.models import Item



# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    card_number = models.PositiveIntegerField(validators=[MinValueValidator(1111111111111111), MaxValueValidator(9999999999999999)])
    cvc = models.PositiveIntegerField(validators=[MinValueValidator(111), MaxValueValidator(999)])
    exp_month = models.PositiveIntegerField(validators=[MaxValueValidator(12)])
    exp_year = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    name = models.CharField(max_length=50)


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    street_number = models.IntegerField()
    city = models.CharField(max_length=50)
    post_code = models.IntegerField()
    #country = models.ForeignKey(Countries, on_delete=models.CASCADE)


class OrderInfo(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer_item', on_delete=models.RESTRICT)
    seller = models.ForeignKey(User, related_name='seller_item',  on_delete=models.RESTRICT)
    item = models.OneToOneField(Item, on_delete=models.RESTRICT)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
