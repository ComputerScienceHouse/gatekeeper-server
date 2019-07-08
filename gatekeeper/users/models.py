from django.contrib.auth.models import AbstractUser
from gatekeeper.models import BaseModel


class User(AbstractUser, BaseModel):
    pass
