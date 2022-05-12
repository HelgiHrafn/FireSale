from django.db import models
from django.contrib.auth.models import User


# Here we probably have models for Items that are available for sale


class Condition(models.Model):
    condition_name = models.CharField(max_length=50)

    def __str__(self):
        return self.condition_name


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_price = models.PositiveIntegerField(max_length=9)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    item_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=50, blank=True)
    item_seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
