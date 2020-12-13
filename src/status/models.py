from django.conf import settings
from django.db import models

class StatusQuerySet(models.QuerySet):
    pass


class StatusManger(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    # like fb, whatsapp instagram status

    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    content = models.TextField(null=True, blank="True")
    image = models.ImageField(upload_to='images', null=True, blank="True")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'
