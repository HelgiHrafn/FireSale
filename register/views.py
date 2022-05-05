from django.shortcuts import render, get_object_or_404, redirect
from register.forms.user_form import UserCreateForm


# Create your views here.
def index(request):
    return render(request, 'register/create_user.html')


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            return redirect('login-index')
    else:
        form = UserCreateForm()
    return render(request, 'register/create_user.html', {
        'form': form
    })

