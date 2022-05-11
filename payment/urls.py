from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_offers
    path('contact_info/<int:bid_id>', views.contact_info, name="payment-contact_info"),
    path('cardinfo/<int:item_id>', views.payment, name="payment-payment"),
    path('review/<int:item_id>', views.review, name="payment-review"),
    path('payment_processed/<int:item_id>', views.payment_processed, name="payment-processed")
]
