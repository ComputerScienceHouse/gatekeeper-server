
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

import secrets
import graphene
from ecdsa import SigningKey, NIST384p
from graphene_django.types import ErrorType
from graphene_django_extras import DjangoSerializerType, LimitOffsetGraphqlPagination
from graphene_django_extras.registry import get_global_registry
from gatekeeper.realms.models import Realm
from gatekeeper.realms.serializers import RealmSerializer


class RealmType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for a Realm'
        serializer_class = RealmSerializer
        output_field_name = 'realm'
        pagination = LimitOffsetGraphqlPagination(default_limit=10, ordering='-slot')
        filter_fields = {
            'id': ['exact', ],
            'name': ['iexact', 'icontains'],
        }


class RealmCreateGenericType(graphene.InputObjectType):
    name = graphene.Field(graphene.String, description="name of the realm")
    slot = graphene.Field(graphene.Int, description="unique slot number for the realm")


class CreateRealm(graphene.Mutation):
    class Arguments:
        new_realm = graphene.Argument(RealmCreateGenericType, required=True)

    ok = graphene.Field(graphene.Boolean, description='Boolean field that return mutation result request.')
    realm = graphene.Field(get_global_registry().get_type_for_model(Realm))
    errors = graphene.List(ErrorType, description='Errors list for the field')

    def mutate(self, info, new_realm: RealmCreateGenericType):
        # Generate transport keys
        read_key = secrets.token_hex(16)
        auth_key = secrets.token_hex(16)
        update_key = secrets.token_hex(16)

        # Generate ECDSA key pair
        sk = SigningKey.generate(curve=NIST384p)
        vk = sk.get_verifying_key()
        private_key = sk.to_pem().decode()
        public_key = vk.to_pem().decode()

        fields = {
            "name": new_realm.name,
            "slot": new_realm.slot,
            "read_key": read_key,
            "auth_key": auth_key,
            "update_key": update_key,
            "private_key": private_key,
            "public_key": public_key
        }

        serializer = RealmSerializer(data=fields)
        if serializer.is_valid():
            realm = serializer.save()
            return CreateRealm(realm=realm, ok=True, errors=None)
        else:
            errors = [
                ErrorType(field=key, messages=value)
                for key, value in serializer.errors.items()
            ]

            return CreateRealm(realm=None, ok=False, errors=errors)


class Query:
    realm, all_realms = RealmType.QueryFields()


class Mutation:
    realm_create = CreateRealm.Field()
    realm_update = RealmType.UpdateField()
    realm_delete = RealmType.DeleteField()
