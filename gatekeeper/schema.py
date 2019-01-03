import graphene
from gatekeeper.access_points.schema import Query as AccessPointQuery
from gatekeeper.access_points.schema import Mutation as AccessPointMutation
from gatekeeper.users.schema import Query as UserQuery
from gatekeeper.users.schema import Mutation as UserMutation
from gatekeeper.groups.schema import Query as GroupQuery
from gatekeeper.groups.schema import Mutation as GroupMutation
from gatekeeper.realms.schema import Query as RealmQuery
from gatekeeper.realms.schema import Mutation as RealmMutation


# This class combines all of the app-level Query objects
class Query(
    AccessPointQuery,
    UserQuery,
    GroupQuery,
    RealmQuery,
    graphene.ObjectType
):
    pass


# This class combines all of the app-level Mutation objects
class Mutation(
    AccessPointMutation,
    UserMutation,
    GroupMutation,
    RealmMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
