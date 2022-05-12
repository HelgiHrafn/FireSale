from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from user.form.profile_form import ProfileForm
from user.models import Profile
from firesale.forms.item_form import ItemCreateForm, ItemImageForm
from firesale.models import Item, ItemImage
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            form.save()
            user_id = User.objects.get(username=form.cleaned_data['username'])
            profile =Profile(user_id=user_id.id)
            profile.save()
            return redirect('login')
        else:
            return render(request, 'user/register.html', {
                'form': UserCreationForm(),
                'message': form.errors
            })

    return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })


@login_required
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


@login_required
def index(request):
    return render(request, 'user/profile.html', {'User': request.user, 'Image': Profile.objects.get(user=request.user.id)})


@login_required
def post_sale(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("item_name")
            price = form.cleaned_data.get("item_price")
            category = form.cleaned_data.get("item_category")
            condition = form.cleaned_data.get("item_condition")
            description = form.cleaned_data.get("item_description")
            item = Item(item_name=name, item_price=price, item_category=category, item_condition=condition,
                        item_description=description, item_seller=request.user)
            item.save()
            return render(request, 'user/post_sale_img_option.html')
    else:
        form = ItemCreateForm()
        #TODO: instance ItemCreateForm()
    return render(request, 'user/post_sale.html', {
        'form': form
    })


def post_sale_images(request):
    form = ItemImageForm()

    if request.method == 'POST':
        form = ItemImageForm(data=request.POST)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            user_id = request.user.id
            item = Item.objects.filter(item_seller_id=user_id).latest('id')
            form = ItemImage(image=image, item_id=item.id)
            form.save()
            counter = ItemImage.objects.filter(item_id=item.id).count()
            print(counter)
            if counter > 2:
                return render(request, 'user/post_sale_images.html', {
                    'message': 'Hámark fjölda mynda náð'
                })
            else:
                form = ItemImageForm()
                return render(request, 'user/post_sale_images.html', {
                    'form': form,
                    'message': 'Setja inn fleiri myndir ?'
                })
        else:
            form = ItemImageForm()
    return render(request, 'user/post_sale_images.html', {
        'form': form,
    })

