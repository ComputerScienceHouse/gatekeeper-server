from django.db import models
from gatekeeper.models import UUIDModel


class AccessPoint(UUIDModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    online = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('allowed_access', 'Allowed access'),
        )

    def __str__(self):
        return self.name
