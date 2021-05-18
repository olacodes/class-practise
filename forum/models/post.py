import uuid
from django.db import models
from django.conf import settings


from .thread import Thread


class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
  post = models.TextField()
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
