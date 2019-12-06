from django.shortcuts import render
from social_django.models import UserSocialAuth

def mypage(request):
    if request.user.is_authenticated:
        user = UserSocialAuth.objects.get(id=request.session['_auth_user_id'])
    else:
        user = ''
    return render(request, 'base.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('/')
