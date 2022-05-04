from django.shortcuts import render
from register.forms.user_form import UserCreateForm


# Create your views here.
def index(request):
    return render(request, 'register/create_user.html')


def create_user(request):
    if request.method == 'POST':
        print(1)
    else:
        form = UserCreateForm()
    return render(request, 'register/create_user.html', {
        'form': form
    })

