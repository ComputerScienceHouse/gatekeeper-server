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

import graphene
from graphene_django import DjangoObjectType
from graphene_django.types import ErrorType
from gatekeeper.configuration.models import Configuration
from gatekeeper.configuration.serializers import ConfigurationSerializer


class ConfigurationType(DjangoObjectType):
    class Meta:
        model = Configuration
        exclude_fields = ['id']


class ConfigurationUpdateGenericType(graphene.InputObjectType):
    system_secret = graphene.Argument(graphene.String, required=True)


class UpdateConfiguration(graphene.Mutation):
    class Arguments:
        new_configuration = graphene.Argument(ConfigurationUpdateGenericType, required=True)

    ok = graphene.Field(graphene.Boolean, description='Boolean field that return mutation result request.')
    configuration = graphene.Field(ConfigurationType)
    errors = graphene.List(ErrorType, description='Errors list for the field')

    def mutate(self, info, new_configuration: ConfigurationUpdateGenericType):
        instance = Configuration.objects.first()
        fields = {
            "system_secret": new_configuration.system_secret
        }

        serializer = ConfigurationSerializer(instance=instance, data=fields)
        if serializer.is_valid():
            config = serializer.save()
            return UpdateConfiguration(configuration=config, ok=True, errors=None)
        else:
            errors = [
                ErrorType(field=key, messages=value)
                for key, value in serializer.errors.items()
            ]

            return UpdateConfiguration(realm=None, ok=False, errors=errors)


class Query:
    configuration = graphene.Field(ConfigurationType)

    def resolve_configuration(self, _):
        return Configuration.objects.first()


class Mutation:
    configuration_update = UpdateConfiguration.Field()
