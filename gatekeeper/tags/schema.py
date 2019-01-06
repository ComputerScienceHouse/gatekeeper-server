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
from gatekeeper.tags.serializers import TagSerializer, TagRealmAssociationSerializer


class TagType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for a Tag'
        serializer_class = TagSerializer
        input_field_name = 'newTag'
        output_field_name = 'tag'
        pagination = LimitOffsetGraphqlPagination(default_limit=10)
        only_fields = ['id', 'created', 'modified', 'user', ]
        filter_fields = {
            'id': ['exact', ],
            'user': ['exact', ]
        }


class TagRealmAssociationType(DjangoSerializerType):
    class Meta:
        description = 'Type definition for a TagRealmAssociation'
        serializer_class = TagRealmAssociationSerializer
        input_field_name = 'newAssociation'
        output_field_name = 'association'
        pagination = LimitOffsetGraphqlPagination()
        filter_fields = {
            'id': ['exact', ],
            'tag': ['exact', ],
            'realm': ['exact', ]
        }


class Query:
    tag, all_tags = TagType.QueryFields()
    tag_realm_association, all_tag_realm_associations = TagRealmAssociationType.QueryFields()


class Mutation:
    tag_create, tag_delete, tag_update = TagType.MutationFields()
    associate_tag_with_realm = TagRealmAssociationType.CreateField()
    dissociate_tag_from_realm = TagRealmAssociationType.DeleteField()
