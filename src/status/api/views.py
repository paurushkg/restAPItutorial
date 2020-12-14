from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication

from status.models import Status
from .serializer import StatusSerializer


class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    # permission_classes = []
    # authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)


class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView
):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # or IsAuthenticated
    # authentication_classes = [SessionAuthentication]
    # queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id')
        query_set = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(query_set, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, *args, **kwargs):
        request = self.request
        passed_id = request.GET.get('id')
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


'''
class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kargs):
        return self.update(request, *args, **kargs)

    def delete(self, request, *args, **kargs):
        return self.destroy(request, *args, **kargs)'''


