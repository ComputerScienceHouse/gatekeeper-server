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
