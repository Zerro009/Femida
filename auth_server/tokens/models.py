from django.db import models

from users.models import *

import secrets

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=1024, blank=True,)

    def save(self, *args, **kwargs):
        self.access_token = secrets.token_hex(nbytes=1024)
        super(Token, self).save(*args, **kwargs)
