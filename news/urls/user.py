from django.contrib import admin
from django.urls import path

from news.apis.v1.user import UserSignUpView, UserSignInView, UserSignOutView,UserInfoView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name="user-signup"),
    path('signin/', UserSignInView.as_view(), name="user-signin"),
    path('signout/', UserSignOutView.as_view(), name="user-signout"),
    path('me/', UserInfoView.as_view(), name="user-me")
]
