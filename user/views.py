from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.form.profile_form import ProfileForm
from user.models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print(form.data)
        if form.is_valid():
            print('check_validity')
            form = form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_edit')

    return render(request, 'user/profile_edit.html', {
        'form': ProfileForm(instance=profile),
    })


def index(request):
    return render(request, 'user/profile.html', {'User': request.user, 'Image': Profile.objects.get(user=request.user.id)})


def profile2(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(instance=user, data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.user = request.user
            user.save()
            return redirect('profile')

    return render(request, 'user/profile.html', {
        'form': UserChangeForm(instance=user),
    })
