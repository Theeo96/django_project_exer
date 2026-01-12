from django.contrib import admin
from django.urls import path

from news.apis.v1.news import NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='newsList')
]