from django.conf.urls import url
from django.contrib import admin
from .views import (
    StatusAPIView,
    StatusDetailAPIView
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>.*)/detail', StatusDetailAPIView.as_view()),

]
