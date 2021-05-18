import uuid

from django.db import models
from django.conf import settings

from .forum import Forum


class Thread(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  topic = models.CharField(max_length=255, null=False)
  description = models.TextField()
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
