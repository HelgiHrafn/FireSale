from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'my_profile/index.html')


def edit_profile(request):
    return render(request, 'my_profile/edit_profile.html')
