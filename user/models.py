from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=15, null=True)
    profile_image = models.CharField(max_length=9999, null=True)
    profile_bio = models.CharField(max_length=50, null=True)
    profile_rating = models.IntegerField(null=True)
    profile_email = models.EmailField(max_length=254, null=True)

