from django.contrib import admin
from django.urls import path

from news.apis.v1.common import HelloWorldView

urlpatterns = [
    path('welcome/', HelloWorldView.as_view(), name='helloWorld')
]
