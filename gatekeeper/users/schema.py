
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
from gatekeeper.users.serializers import UserSerializer


class UserType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for a User'
        serializer_class = UserSerializer
        input_field_name = 'newUser'
        output_field_name = 'user'
        pagination = LimitOffsetGraphqlPagination(default_limit=10, ordering='-username')
        filter_fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }


class Query:
    user, all_users = UserType.QueryFields()


class Mutation:
    user_create, user_delete, user_update = UserType.MutationFields()
