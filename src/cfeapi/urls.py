from django.conf.urls import url, include
from django.contrib import admin

from updates.views import(
    json_example,
    JsonExampleCBV,
    JsonExampleCBV2,
    SerializedListView,
    SerializedDetailView
)

urlpatterns = [
    url(r'^api/status/', include('status.api.urls')),

    url(r'^$', json_example),
    url(r'^one', JsonExampleCBV.as_view()),
    url(r'^two', JsonExampleCBV2.as_view()),
    url(r'^serailized/list', SerializedListView.as_view()),
    url(r'^serailized/detail', SerializedDetailView.as_view()),

    url(r'^admin/', admin.site.urls),
]
