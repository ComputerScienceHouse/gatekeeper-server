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
from gatekeeper.groups.serializers import GroupSerializer


class GroupType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for a Group'
        serializer_class = GroupSerializer
        input_field_name = 'newGroup'
        output_field_name = 'group'
        pagination = LimitOffsetGraphqlPagination(default_limit=10, ordering='-name')
        filter_fields = {
            'name': ['exact', 'icontains'],
        }


class Query:
    group, all_groups = GroupType.QueryFields()


class Mutation:
    group_create, group_delete, group_update = GroupType.MutationFields()
