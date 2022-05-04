from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/login
    path('create_user', views.create_user, name='create_user'),
    path('', views.create_user, name="register-create-user"),
]
