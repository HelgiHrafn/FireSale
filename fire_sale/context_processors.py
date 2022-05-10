# project/context_processors.py
from user.models import Profile
# project/context_processors.py


def user_img(request):
    user = request.user.id
    if user:
        user_id = request.user.id
        profile = Profile.objects.get(user_id=user_id)
        profile_image = profile.profile_image
        return {'profile_img': profile_image}


