from django.db import models

from users.models import *

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    access_token = models.CharField(max_length=1024, blank=True,)
    refresh_token = models.CharField(max_length=1024, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)
