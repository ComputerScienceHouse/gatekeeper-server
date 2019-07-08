
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
from gatekeeper.models import BaseModel


class Realm(BaseModel):
    name = models.CharField(max_length=100)
    slot = models.IntegerField()
    read_key = models.CharField(max_length=32)
    auth_key = models.CharField(max_length=32)
    update_key = models.CharField(max_length=32)
    public_key = models.TextField(help_text='public key in X.509 PEM format')
    private_key = models.TextField(help_text='private key in X.509 PEM format')

    def __str__(self):
        return self.name
