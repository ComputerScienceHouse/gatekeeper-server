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
