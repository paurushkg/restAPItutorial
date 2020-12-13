from django.conf.urls import url
from django.contrib import admin
from .views import (
    StatusAPIView,
    StatusAPIDetailView
)

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>.*)/$', StatusAPIDetailView.as_view()),

]
