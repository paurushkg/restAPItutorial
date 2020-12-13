from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from .models import Update


def json_example(request):
    data = {
        "count": "1",
        "hello": "heelo"
    }
    return JsonResponse(data)


class JsonExampleCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": "1",
            "hello": "CBV heelo"
        }
        return JsonResponse(data)


class JsonResponseMixin(object):
    def render_to_json_response(self,context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


class JsonExampleCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": "1",
            "hello": "CBV2 heelo"
        }
        return self.render_to_json_response(data)


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        data = Update.objects.all().serialize()
        return HttpResponse(data, content_type='application/json')


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.filter(id=1)
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')


