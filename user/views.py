from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.form.profile_form import ProfileForm
from user.models import Profile
from firesale.forms.item_form import ItemCreateForm, ItemImageForm
from firesale.models import Item, ItemImage


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
            condition = form.cleaned_data.get("item_condition")
            description = form.cleaned_data.get("item_description")
            item = Item(item_name=name, item_price=price, item_condition=condition,
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
            counter = ItemImage.objects.filter(item_id=item.id).count()
            if counter == 2:
                return render(request, 'user/post_sale_images.html', {
                    'message': 'Hámark fjölda mynda náð'
                })
            else:
                form = ItemImage(image=image, item_id=item.id)
                form.save()
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

