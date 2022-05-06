from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.form.profile_form import ProfileForm
from user.models import Profile
from firesale.forms.item_form import ItemCreateForm
from firesale.models import Item


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


def post_sale(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("item_name")
            price = form.cleaned_data.get("item_price")
            image = form.cleaned_data.get("item_image")
            condition = form.cleaned_data.get("item_condition")
            description = form.cleaned_data.get("item_description")
            item = Item(item_name=name, item_price=price, item_image=image, item_condition=condition,
                        item_description=description, item_seller=request.user)
            item.save()
            return redirect('profile')
    else:
        form = ItemCreateForm()
        #TODO: instance ItemCreateForm()
    return render(request, 'user/post_sale.html', {
        'form': form
    })


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
