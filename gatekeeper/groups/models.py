from django.contrib.auth.models import Group
from gatekeeper.models import BaseModel


def configure_group_model():
    fields = BaseModel._meta.get_fields()

    for field in fields:
        if not hasattr(Group, field.name):
            field.contribute_to_class(Group, field.name)
