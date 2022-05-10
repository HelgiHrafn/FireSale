# project/context_processors.py
#from user.models import Profile
# project/context_processors.py

def user_img(request):
    return {'profile_img': 'https://media.istockphoto.com/vectors/user-icon-flat-isolated-on-white-background-user-symbol-vector-vector-id1300845620?k=20&m=1300845620&s=612x612&w=0&h=f4XTZDAv7NPuZbG0habSpU0sNgECM0X7nbKzTUta3n8='}

#def user_img(request):
#    user = request.user.id
#    if user:
#        user_id = request.user.id
#        profile = Profile.objects.get(user_id=user_id)
#        profile_image = profile.profile_image
#        return {'profile_img': profile_image}


