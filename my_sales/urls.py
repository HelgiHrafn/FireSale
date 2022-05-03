from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/my_sales
    path('', views.index, name="my_sales-index"),
]