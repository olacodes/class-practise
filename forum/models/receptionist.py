from django.db import models
from django.conf import settings


class Receptionist(models.Model):
  GENDER = [("M", "Male"), ("F", "Female")]
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  gender = models.CharField(max_length=10, choices=GENDER)


