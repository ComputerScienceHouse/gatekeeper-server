import graphene
from gatekeeper.access_points.schema import Query as AccessPointQuery
from gatekeeper.access_points.schema import Mutation as AccessPointMutation
from gatekeeper.users.schema import Query as UserQuery
from gatekeeper.users.schema import Mutation as UserMutation
from gatekeeper.groups.schema import Query as GroupQuery
from gatekeeper.groups.schema import Mutation as GroupMutation


# This class combines all of the app-level Query objects
class Query(
    AccessPointQuery,
    UserQuery,
    GroupQuery,
    graphene.ObjectType
):
    pass


# This class combines all of the app-level Mutation objects
class Mutation(
    AccessPointMutation,
    UserMutation,
    GroupMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
