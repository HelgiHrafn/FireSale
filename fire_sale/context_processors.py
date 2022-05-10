# project/context_processors.py
from user.models import Profile


def user_img(request):
    user_id = request.user.id
    if user_id:
        profile_img = Profile.objects.get(user_id=user_id)
        return {
            'profile_image': profile_img,
            }
    else:
        profile_img = Profile.objects.all()[:1].get()
        return {'profile_image': profile_img}
