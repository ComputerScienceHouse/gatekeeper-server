# Gatekeeper - Open source access control
# Copyright (C) 2018-2019 Steven Mirabito
#
# This file is part of Gatekeeper.
#
# Gatekeeper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gatekeeper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gatekeeper.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User
from gatekeeper.models import UUIDModel
from gatekeeper.realms.models import Realm


class Tag(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    realms = models.ManyToManyField(Realm, through='TagRealmAssociation')

    def __str__(self):
        return f"{self.id}, user='{self.user.username}'"


class TagRealmAssociation(UUIDModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('tag', 'realm'),)
