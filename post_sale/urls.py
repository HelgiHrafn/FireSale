from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/post_sale
    path('', views.index, name="post_sale-index"),
]
