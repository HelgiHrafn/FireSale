from django.db import models
from login.models import User

# Here we probably have models for Items that are available for sale


class Condition(models.Model):
    condition_name = models.CharField(max_length=50)

    def __str__(self):
        return self.condition_name


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=9999)
    item_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=150)
    item_seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


