from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/firesale
    path('', views.index, name="firesale-index"),
    path('<opt>', views.index, name="firesale-index"),
    path('<int:id>', views.get_item_by_id, name="item-details"),
    path('item_bid/<int:id>/', views.bid_item_by_id, name="item-bid"),
]
