from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_profile
    path('', views.index, name="my_profile-index"),
    path('/edit_profile', views.edit_profile, name="my_profile-edit_profile")
]
