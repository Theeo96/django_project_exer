from django.contrib import admin
from django.urls import path

from news.apis.v1.sample import SampleListView, SampleDetailView

urlpatterns = [
    path('', SampleListView.as_view(), name='sampleList'),
    path('<int:sample_id>', SampleDetailView.as_view(), name='sampleDetail')
]
