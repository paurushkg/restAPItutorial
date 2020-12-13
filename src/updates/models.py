from django.core.serializers import serialize

from django.conf import settings
from django.db import models


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        return serialize('json', qs,fields=('user', 'content', 'image'))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pics', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        return serialize('json', [self], fields=('user', 'content', 'image'))
