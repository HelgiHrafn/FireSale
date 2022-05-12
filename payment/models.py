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
    cvc = models.IntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
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
    country = CountryField(countries_flag_url='//investmentbank.com/wp-content/uploads/2012/11/fire-sale-for-mergers-and-acquisitions-1-1-768x512.jpg')



class OrderInfo(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer_item', on_delete=models.RESTRICT)
    seller = models.ForeignKey(User, related_name='seller_item',  on_delete=models.RESTRICT)
    item = models.OneToOneField(Item, on_delete=models.RESTRICT)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
