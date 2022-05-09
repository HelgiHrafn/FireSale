from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.index, name='profile'),
    path('profile_edit', views.profile, name='profile_edit'),
    path('post_sale', views.post_sale, name='post_sale'),
    path('post_sale_images', views.post_sale_images, name='post_sale_images'),
]
