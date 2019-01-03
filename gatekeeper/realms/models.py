from django.db import models
from gatekeeper.models import UUIDModel


class Realm(UUIDModel):
    name = models.CharField(max_length=100)
    slot = models.IntegerField()
    read_key = models.CharField(max_length=32)
    auth_key = models.CharField(max_length=32)
    update_key = models.CharField(max_length=32)
    public_key = models.TextField(help_text='public key in X.509 PEM format')
    private_key = models.TextField(help_text='private key in X.509 PEM format')

    def __str__(self):
        return self.name
