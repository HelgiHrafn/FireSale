from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_offers
    path('cardinfo', views.payment, name="payment-payment"),
    path('contact_info', views.contact_info, name="payment-contact_info"),
    path('review', views.review, name="payment-review")
]
