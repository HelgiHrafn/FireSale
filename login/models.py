from django.db import models

# Create your models here.


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserProfile(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    profile_rating = models.IntegerField()