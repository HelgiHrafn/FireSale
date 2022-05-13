from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from firesale.models import Item
from django_countries.fields import CountryField


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    card_number = models.BigIntegerField()
    cvc = models.PositiveIntegerField()
    exp_month = models.PositiveIntegerField()
    exp_year = models.PositiveIntegerField()
    name = models.CharField(max_length=50)


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    street_number = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    post_code = models.IntegerField()
    country = CountryField(countries_flag_url='//investmentbank.com/wp-content/uploads/2012/11/fire-sale-for-mergers-and-acquisitions-1-1-768x512.jpg')



class OrderInfo(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer_item', on_delete=models.RESTRICT)
    seller = models.ForeignKey(User, related_name='seller_item',  on_delete=models.RESTRICT)
    item = models.OneToOneField(Item, on_delete=models.RESTRICT)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
