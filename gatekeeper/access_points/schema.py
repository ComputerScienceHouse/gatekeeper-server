
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

from graphene_django_extras import DjangoSerializerType, LimitOffsetGraphqlPagination
from gatekeeper.access_points.serializers import AccessPointSerializer


class AccessPointType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for an Access Point'
        serializer_class = AccessPointSerializer
        input_field_name = 'newAccessPoint'
        output_field_name = 'accessPoint'
        pagination = LimitOffsetGraphqlPagination(default_limit=10, ordering='-name')
        filter_fields = {
            'id': ['exact', ],
            'name': ['iexact', 'icontains'],
            'location': ['iexact', 'icontains'],
        }


class Query:
    access_point, all_access_points = AccessPointType.QueryFields()


class Mutation:
    access_point_create, access_point_delete, access_point_update = AccessPointType.MutationFields()
