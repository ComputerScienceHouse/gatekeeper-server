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
