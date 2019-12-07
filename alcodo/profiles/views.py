from django.shortcuts import render
from django.shortcuts import redirect

# from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from django.contrib.auth import logout

def mypage(request):
    # print(request.session['_auth_user_id'])
    if request.user.is_authenticated:
        print(request.session['_auth_user_id'])
        user = User.objects.get(id=request.session['_auth_user_id'])
    else:
        user = None
    return render(request, 'base.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('/')
