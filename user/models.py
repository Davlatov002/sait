from django.db import models
import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    wallet_id = models.CharField(max_length=200, blank=True, null=True, unique=True)
    blanse = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=200, blank=False, null=False, unique=True)
    password = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.email