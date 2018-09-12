import uuid
import graphene
from django.db import models
from graphene.relay import Connection


class UUIDModel(models.Model):
    """
    An abstract base class model that provides a UUID as the primary key.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CountableConnection(Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, _):
        return self.length
