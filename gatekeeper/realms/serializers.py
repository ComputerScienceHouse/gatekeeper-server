
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

from rest_framework.serializers import ModelSerializer
from gatekeeper.realms.models import Realm


class RealmSerializer(ModelSerializer):
    class Meta:
        model = Realm
        fields = [
            'name',
            'slot',
            'read_key',
            'auth_key',
            'update_key',
            'public_key',
            'private_key'
        ]
