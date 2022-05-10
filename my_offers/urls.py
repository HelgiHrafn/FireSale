from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_offers
    path('', views.index, name="my-offers-index"),
]
