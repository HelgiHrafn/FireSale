from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_sales
    path('', views.index, name="my_sales-index"),
    path('<int:id>', views.get_item_by_id, name="item-details"),
    path('<int:id>/accept_bid/<int:bid>', views.accept_bid, name="sell-confirm"),
]
