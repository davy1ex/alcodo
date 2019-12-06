from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url

import profiles.views


SOCIAL_AUTH_URL_NAMESPACE = 'social'
urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url('logout/', profiles.views.logout_view, name='logout'),
    path('', profiles.views.mypage),
]
