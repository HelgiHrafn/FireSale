from django.shortcuts import render
from login.models import User


# Create your views here.
def index(request):
    return render(request, 'login/index.html',  {
        'users': User.objects.all()
    })
