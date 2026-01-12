"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework import viewsets

from news.models.news import NewsItem
from news.serializers.news import NewsItemSerializer

class NewsViewSet(viewsets.ModelViewSet) :
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('v1/common/welcome/', HelloWorldView.as_view(), name='helloWorld'),
    # path('v1/samples/', SampleListView.as_view(), name='sampleList'),
    # path('v1/samples/<int:sample_id>', SampleDetailView.as_view(), name='sampleDetail')
    path('v1/common/', include('news.urls.common')),
    path('v1/samples/', include('news.urls.sample')),
    path('v1/user/', include('news.urls.user')),
    path('v1/news/', include('news.urls.news')),
    path('api/', include(router.urls))
]
